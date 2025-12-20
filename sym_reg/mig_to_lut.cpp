/* 
 * 使用 mockturtle 将 AIG/MIG 转换为 LUT 并获取物理信息
 * 
 * 编译命令（需要先编译 mockturtle）:
 * g++ -std=c++17 mig_to_lut.cpp -o mig_to_lut \
 *     -I../mockturtle/include \
 *     -I../mockturtle/experiments \
 *     -L../mockturtle/build \
 *     -lmockturtle -llorina -lfmt -lpthread
 * 
 * 或者使用 CMake（推荐）
 */

#include <iostream>
#include <fstream>
#include <string>
#include <lorina/aiger.hpp>
#include <mockturtle/io/aiger_reader.hpp>
#include <mockturtle/networks/aig.hpp>
#include <mockturtle/networks/mig.hpp>
#include <mockturtle/networks/klut.hpp>
#include <mockturtle/algorithms/lut_mapping.hpp>
#include <mockturtle/algorithms/collapse_mapped.hpp>
#include <mockturtle/views/mapping_view.hpp>
#include <mockturtle/views/depth_view.hpp>

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " <input.aig> <output_stats.txt>" << std::endl;
        std::cerr << "Converts AIG/MIG to LUT and extracts physical statistics" << std::endl;
        return 1;
    }

    std::string input_file = argv[1];
    std::string output_file = argv[2];

    // 读取 AIG（mockturtle 可以从 AIG 读取，然后转换为 MIG）
    aig_network aig;
    if (lorina::read_aiger(input_file, mockturtle::aiger_reader(aig)) != lorina::return_code::success) {
        std::cerr << "Error reading AIG file: " << input_file << std::endl;
        return 1;
    }

    // 执行 LUT mapping
    mockturtle::lut_mapping_params ps;
    mockturtle::lut_mapping_stats st;
    mockturtle::mapping_view<aig_network, true> mapped_aig{aig};
    mockturtle::lut_mapping<decltype(mapped_aig), true>(mapped_aig, ps, &st);
    
    // 转换为 k-LUT 网络
    const auto klut = *mockturtle::collapse_mapped_network<mockturtle::klut_network>(mapped_aig);
    
    // 计算深度
    mockturtle::depth_view<mockturtle::klut_network> klut_depth{klut};
    uint32_t depth = klut_depth.depth();
    
    // 计算面积（LUT 数量）
    uint32_t area = klut.num_gates();
    
    // 计算延迟
    // 注意：mockturtle 的 LUT mapping 可能不直接提供延迟信息
    // 这里使用深度作为延迟的近似值
    // 如果需要准确的延迟，需要配置 LUT 库
    double delay = static_cast<double>(depth);
    
    // 写入统计信息
    std::ofstream out(output_file);
    if (!out.is_open()) {
        std::cerr << "Error opening output file: " << output_file << std::endl;
        return 1;
    }
    
    out << "area: " << area << std::endl;
    out << "delay: " << delay << std::endl;
    out << "depth: " << depth << std::endl;
    out << "lev: " << depth << std::endl;  // lev 通常等于 depth
    out << "luts: " << area << std::endl;
    out << "power: 0.0" << std::endl;  // 需要根据 LUT 库计算
    out.close();

    std::cout << "LUT mapping completed: area=" << area 
              << ", delay=" << delay 
              << ", depth=" << depth << std::endl;

    return 0;
}
