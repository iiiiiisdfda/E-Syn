import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(script_dir, '..')
input_csv_path = os.path.join(parent_dir, 'sorted_delay.csv')
output_csv_product_path = os.path.join(parent_dir, 'area_delay_product_total.csv')
output_csv_pareto_path = os.path.join(parent_dir, 'pareto_optimal_points.csv')

data = pd.read_csv(input_csv_path)
area = data['Area']
delay = data['Delay']
data = np.column_stack((area, delay))

# Finding Pareto optimal points
pareto_optimal_points = []
for i in range(len(data)):
    is_pareto_optimal = True
    for j in range(len(data)):
        if j != i and (data[j][0] <= data[i][0] and data[j][1] <= data[i][1]):
            is_pareto_optimal = False
            break
    if is_pareto_optimal:
        pareto_optimal_points.append(data[i])

# Separate x and y coordinates
x_pareto = [point[0] for point in pareto_optimal_points]
y_pareto = [point[1] for point in pareto_optimal_points]

# # Calculate R-method scores
# p1 = 1
# p2 = (1 / (1 + 1 / 2))
# pt = p1 + p2
# w1 = p1 / pt
# w2 = p2 / pt
scores1 = []
for point in data:
    #score = point[1]
    score = point[0] * point[1]
    scores1.append(score)

sorted_indices1 = np.argsort(scores1)
sorted_points1 = [data[i] for i in sorted_indices1]
sorted_scores1 = [scores1[i] for i in sorted_indices1]

data0 = []
for i in range(len(sorted_points1)):
    point = sorted_points1[i]
    delay = point[0]
    area = point[1]
    score = sorted_scores1[i]
    data0.append([i, delay, area, score])


scores = []
for point in pareto_optimal_points:
   # score = point[0] * point[1]
    score = point[0]
    scores.append(score)
   # print("points:", point, "scores:", score)

filename = output_csv_product_path
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Point", "Delay", "Area", "Score"])  
    writer.writerows(data0)  

# Find the best score point
# Sort Pareto optimal points based on scores
sorted_indices = np.argsort(scores)
sorted_points = [pareto_optimal_points[i] for i in sorted_indices]
sorted_scores = [scores[i] for i in sorted_indices]

# Print sorted points and scores
for i in range(len(sorted_points)):
    print("points:", sorted_points[i], "scores:", sorted_scores[i])

# Find the best score point
best_index = np.argmin(sorted_scores)
best_point = sorted_points[best_index]
print("best_point:", best_point)

data1 = []
for i in range(len(sorted_points)):
    point = sorted_points[i]
    delay = point[0]
    area = point[1]
    score = sorted_scores[i]
    data1.append([i, delay, area, score])


filename = output_csv_pareto_path
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Point", "Delay", "Area", "Score"])  
    writer.writerows(data1)  


# Scatter plot
# plt.scatter(data[:, 0], data[:, 1], color='red', label='Non-Pareto Points')
# plt.scatter(x_pareto, y_pareto, color='blue', label='Pareto Optimal Points')
# plt.scatter(best_point[0], best_point[1], color='green', s=100, label='Best Point')

# # Add legend and labels
# plt.legend()
# plt.xlabel('Area')
# plt.ylabel('Delay')

# # Display the plot
# plt.show()