def score(input):
    if input[7] < 128.0:
        if input[7] < 58.0:
            var0 = 0.09713098
        else:
            var0 = 0.097767256
    else:
        if input[7] < 299.0:
            var0 = 0.09813459
        else:
            var0 = 0.09840027
    if input[7] < 129.0:
        if input[7] < 64.0:
            var1 = 0.09693212
        else:
            var1 = 0.09756402
    else:
        if input[7] < 304.0:
            var1 = 0.09794647
        else:
            var1 = 0.09823713
    if input[7] < 151.0:
        if input[7] < 72.0:
            if input[7] < 41.0:
                var2 = 0.09597906
            else:
                var2 = 0.09686624
        else:
            var2 = 0.09741046
    else:
        if input[7] < 304.0:
            var2 = 0.0977669
        else:
            var2 = 0.09805516
    if input[7] < 127.0:
        if input[7] < 63.0:
            var3 = 0.096259795
        else:
            var3 = 0.09702812
    else:
        if input[7] < 299.0:
            var3 = 0.09749507
        else:
            var3 = 0.097852044
    if input[7] < 125.0:
        if input[7] < 58.0:
            var4 = 0.09577549
        else:
            var4 = 0.09669065
    else:
        if input[7] < 299.0:
            var4 = 0.09723521
        else:
            if input[30] < 15.0:
                var4 = 0.09748665
            else:
                var4 = 0.097734824
    if input[7] < 128.0:
        if input[7] < 63.0:
            if input[7] < 38.0:
                var5 = 0.09445398
            else:
                var5 = 0.095662594
        else:
            var5 = 0.09639513
    else:
        if input[7] < 307.0:
            if input[30] < 14.0:
                var5 = 0.09680157
            else:
                var5 = 0.097086795
        else:
            var5 = 0.09739432
    if input[7] < 128.0:
        if input[7] < 63.0:
            if input[7] < 38.0:
                var6 = 0.093904674
            else:
                var6 = 0.09522719
        else:
            var6 = 0.09603033
    else:
        if input[7] < 307.0:
            if input[30] < 13.0:
                var6 = 0.09643957
            else:
                var6 = 0.09676599
        else:
            if input[30] < 15.0:
                var6 = 0.096954204
            else:
                var6 = 0.0972518
    if input[7] < 153.0:
        if input[7] < 71.0:
            if input[7] < 41.0:
                var7 = 0.093521334
            else:
                var7 = 0.09491155
        else:
            if input[7] < 106.0:
                var7 = 0.09552566
            else:
                var7 = 0.09598266
    else:
        if input[7] < 329.0:
            if input[30] < 14.0:
                var7 = 0.09619352
            else:
                var7 = 0.09653174
        else:
            if input[30] < 15.0:
                var7 = 0.09666487
            else:
                var7 = 0.0969868
    if input[7] < 155.0:
        if input[7] < 71.0:
            if input[7] < 41.0:
                var8 = 0.09288628
            else:
                var8 = 0.09440495
        else:
            if input[7] < 106.0:
                var8 = 0.09507717
            else:
                var8 = 0.09558251
    else:
        if input[7] < 319.0:
            if input[30] < 14.0:
                var8 = 0.095804185
            else:
                var8 = 0.096178204
        else:
            if input[30] < 14.0:
                var8 = 0.09627866
            else:
                var8 = 0.09664569
    if input[7] < 153.0:
        if input[7] < 71.0:
            if input[7] < 41.0:
                var9 = 0.09219393
            else:
                var9 = 0.09385103
        else:
            if input[7] < 106.0:
                var9 = 0.09458616
            else:
                var9 = 0.09513443
    else:
        if input[7] < 329.0:
            if input[30] < 13.0:
                var9 = 0.09533749
            else:
                var9 = 0.095763676
        else:
            if input[30] < 15.0:
                var9 = 0.0959548
            else:
                var9 = 0.09634303
    if input[7] < 155.0:
        if input[7] < 71.0:
            if input[7] < 41.0:
                var10 = 0.09144015
            else:
                var10 = 0.093246005
        else:
            if input[7] < 106.0:
                var10 = 0.09404909
            else:
                var10 = 0.094654225
    else:
        if input[7] < 316.0:
            if input[30] < 14.0:
                var10 = 0.09492091
            else:
                var10 = 0.09536438
        else:
            if input[30] < 15.0:
                var10 = 0.095533244
            else:
                var10 = 0.095961265
    if input[7] < 154.0:
        if input[7] < 71.0:
            if input[7] < 41.0:
                var11 = 0.09062066
            else:
                var11 = 0.09258595
        else:
            if input[7] < 106.0:
                var11 = 0.09346226
            else:
                var11 = 0.094120994
    else:
        if input[7] < 329.0:
            if input[30] < 13.0:
                var11 = 0.094363995
            else:
                var11 = 0.09487535
        else:
            if input[30] < 15.0:
                var11 = 0.09510106
            else:
                var11 = 0.095567614
    if input[7] < 154.0:
        if input[7] < 71.0:
            if input[7] < 41.0:
                var12 = 0.08973115
            else:
                var12 = 0.091866754
        else:
            if input[7] < 106.0:
                var12 = 0.09282177
            else:
                var12 = 0.09354078
    else:
        if input[7] < 329.0:
            if input[30] < 14.0:
                var12 = 0.09387248
            else:
                var12 = 0.094406
        else:
            if input[30] < 15.0:
                var12 = 0.09461229
            else:
                var12 = 0.09512313
    if input[7] < 155.0:
        if input[7] < 71.0:
            if input[7] < 41.0:
                var13 = 0.08876728
            else:
                var13 = 0.09108421
        else:
            if input[7] < 106.0:
                var13 = 0.09212359
            else:
                var13 = 0.09291031
    else:
        if input[7] < 347.0:
            if input[30] < 13.0:
                var13 = 0.093221076
            else:
                var13 = 0.09383624
        else:
            if input[30] < 15.0:
                var13 = 0.09409721
            else:
                var13 = 0.094655134
    if input[7] < 154.0:
        if input[7] < 71.0:
            if input[7] < 38.0:
                var14 = 0.08731466
            else:
                var14 = 0.09016784
        else:
            if input[7] < 106.0:
                var14 = 0.09136353
            else:
                if input[30] < 14.0:
                    var14 = 0.091836415
                else:
                    var14 = 0.0925714
    else:
        if input[7] < 347.0:
            if input[30] < 13.0:
                var14 = 0.09255646
            else:
                var14 = 0.09322503
        else:
            if input[30] < 14.0:
                var14 = 0.09344161
            else:
                if input[12] < 0.19248678:
                    var14 = 0.0936879
                else:
                    var14 = 0.094253324
    if input[7] < 155.0:
        if input[7] < 71.0:
            if input[7] < 41.0:
                var15 = 0.086595014
            else:
                var15 = 0.08931257
        else:
            if input[7] < 106.0:
                if input[30] < 13.0:
                    var15 = 0.09005432
                else:
                    var15 = 0.09094622
            else:
                if input[30] < 14.0:
                    var15 = 0.091063775
                else:
                    var15 = 0.091845326
    else:
        if input[7] < 329.0:
            if input[30] < 14.0:
                if input[12] < 0.19248678:
                    var15 = 0.09142255
                else:
                    var15 = 0.09218912
            else:
                var15 = 0.09259442
        else:
            if input[30] < 15.0:
                if input[12] < 0.20056497:
                    var15 = 0.0923511
                else:
                    var15 = 0.09311006
            else:
                if input[12] < 0.18503119:
                    var15 = 0.09307835
                else:
                    var15 = 0.09368526
    if input[7] < 154.0:
        if input[7] < 71.0:
            if input[7] < 38.0:
                var16 = 0.084905885
            else:
                var16 = 0.088236526
        else:
            if input[7] < 106.0:
                if input[30] < 13.0:
                    var16 = 0.089117154
                else:
                    var16 = 0.09008425
            else:
                if input[30] < 14.0:
                    var16 = 0.090198085
                else:
                    var16 = 0.09106703
    else:
        if input[7] < 329.0:
            if input[30] < 14.0:
                if input[12] < 0.19414414:
                    var16 = 0.090613715
                else:
                    var16 = 0.09144043
            else:
                var16 = 0.091868535
        else:
            if input[30] < 15.0:
                if input[12] < 0.20056497:
                    var16 = 0.091611095
                else:
                    var16 = 0.09243774
            else:
                if input[12] < 0.18503119:
                    var16 = 0.09240318
                else:
                    var16 = 0.093065076
    if input[7] < 155.0:
        if input[7] < 73.0:
            if input[7] < 41.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var17 = 0.081581846
                    else:
                        var17 = 0.04284333
                else:
                    var17 = 0.08475366
            else:
                var17 = 0.087302715
        else:
            if input[30] < 14.0:
                if input[7] < 104.0:
                    var17 = 0.08820168
                else:
                    var17 = 0.089269295
            else:
                if input[7] < 106.0:
                    var17 = 0.089278854
                else:
                    var17 = 0.09020852
    else:
        if input[7] < 326.0:
            if input[30] < 14.0:
                if input[12] < 0.19414414:
                    var17 = 0.089718066
                else:
                    var17 = 0.09062233
            else:
                if input[11] < 0.24438202:
                    var17 = 0.09127034
                else:
                    var17 = 0.090484895
        else:
            if input[30] < 15.0:
                if input[12] < 0.20056497:
                    var17 = 0.09079712
                else:
                    var17 = 0.09169819
            else:
                if input[7] < 765.0:
                    var17 = 0.09195196
                else:
                    var17 = 0.09262078
    if input[7] < 155.0:
        if input[7] < 73.0:
            if input[7] < 41.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var18 = 0.080018364
                    else:
                        var18 = 0.040834766
                else:
                    var18 = 0.08340562
            else:
                var18 = 0.08614444
        else:
            if input[30] < 14.0:
                if input[7] < 104.0:
                    var18 = 0.08711385
                else:
                    var18 = 0.08826735
            else:
                if input[7] < 106.0:
                    var18 = 0.08827773
                else:
                    var18 = 0.08928422
    else:
        if input[7] < 329.0:
            if input[30] < 14.0:
                if input[12] < 0.19414414:
                    var18 = 0.08875548
                else:
                    var18 = 0.08973435
            else:
                if input[11] < 0.24438202:
                    var18 = 0.09044359
                else:
                    var18 = 0.08959318
        else:
            if input[30] < 15.0:
                if input[12] < 0.20056497:
                    var18 = 0.089932516
                else:
                    var18 = 0.09090884
            else:
                if input[7] < 765.0:
                    var18 = 0.09117834
                else:
                    var18 = 0.09190469
    if input[7] < 155.0:
        if input[7] < 71.0:
            if input[7] < 38.0:
                var19 = 0.08059993
            else:
                if input[7] < 50.0:
                    var19 = 0.08351936
                else:
                    var19 = 0.08512059
        else:
            if input[7] < 106.0:
                if input[30] < 13.0:
                    var19 = 0.08582275
                else:
                    var19 = 0.087048784
            else:
                if input[30] < 14.0:
                    var19 = 0.0872068
                else:
                    var19 = 0.0882835
    else:
        if input[7] < 347.0:
            if input[30] < 13.0:
                if input[12] < 0.19354838:
                    var19 = 0.08757667
                else:
                    var19 = 0.08870482
            else:
                if input[11] < 0.24438202:
                    if input[7] < 205.0:
                        var19 = 0.088968866
                    else:
                        var19 = 0.089741185
                else:
                    var19 = 0.088602096
        else:
            if input[30] < 14.0:
                if input[12] < 0.20295984:
                    var19 = 0.088922195
                else:
                    var19 = 0.08995643
            else:
                if input[12] < 0.19248678:
                    var19 = 0.08997822
                else:
                    var19 = 0.090856954
    if input[7] < 155.0:
        if input[7] < 73.0:
            if input[7] < 41.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var20 = 0.07654231
                    else:
                        var20 = 0.03485447
                else:
                    var20 = 0.08043049
            else:
                if input[30] < 13.0:
                    var20 = 0.08296981
                else:
                    var20 = 0.08433629
        else:
            if input[30] < 14.0:
                if input[7] < 104.0:
                    var20 = 0.08467796
                else:
                    var20 = 0.08601768
            else:
                if input[7] < 110.0:
                    var20 = 0.08610649
                else:
                    var20 = 0.08724665
    else:
        if input[7] < 347.0:
            if input[30] < 13.0:
                if input[12] < 0.19354838:
                    var20 = 0.0864397
                else:
                    var20 = 0.087657146
            else:
                if input[11] < 0.24438202:
                    if input[7] < 205.0:
                        var20 = 0.08794251
                    else:
                        var20 = 0.088778
                else:
                    var20 = 0.08754619
        else:
            if input[30] < 14.0:
                if input[12] < 0.20295984:
                    var20 = 0.08789208
                else:
                    var20 = 0.089011095
            else:
                if input[12] < 0.19248678:
                    var20 = 0.0890347
                else:
                    var20 = 0.08998735
    if input[7] < 155.0:
        if input[7] < 73.0:
            if input[7] < 41.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var21 = 0.07467948
                    else:
                        var21 = 0.033059414
                else:
                    var21 = 0.07879223
            else:
                if input[30] < 13.0:
                    var21 = 0.08149671
                else:
                    var21 = 0.082958184
        else:
            if input[30] < 14.0:
                if input[7] < 104.0:
                    var21 = 0.0833241
                else:
                    var21 = 0.08476177
            else:
                if input[7] < 106.0:
                    var21 = 0.08477556
                else:
                    var21 = 0.086036645
    else:
        if input[7] < 347.0:
            if input[30] < 13.0:
                if input[12] < 0.19354838:
                    if input[5] < 1883.0:
                        var21 = 0.08522091
                    else:
                        var21 = 0.035298433
                else:
                    var21 = 0.08652642
            else:
                if input[11] < 0.25714287:
                    if input[7] < 205.0:
                        var21 = 0.08680483
                    else:
                        var21 = 0.08769424
                else:
                    var21 = 0.086243235
        else:
            if input[30] < 14.0:
                if input[12] < 0.20295984:
                    var21 = 0.0867798
                else:
                    var21 = 0.08798815
            else:
                if input[12] < 0.19248678:
                    var21 = 0.088013664
                else:
                    if input[7] < 819.0:
                        var21 = 0.08874999
                    else:
                        var21 = 0.0895443
    if input[7] < 155.0:
        if input[7] < 71.0:
            if input[7] < 38.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var22 = 0.072719745
                    else:
                        var22 = 0.031324483
                else:
                    var22 = 0.07652222
            else:
                if input[7] < 50.0:
                    if input[10] < 0.11857708:
                        var22 = 0.02895433
                    else:
                        var22 = 0.07890651
                else:
                    var22 = 0.08087876
        else:
            if input[7] < 106.0:
                if input[30] < 13.0:
                    var22 = 0.08172701
                else:
                    var22 = 0.083248965
            else:
                if input[30] < 14.0:
                    var22 = 0.08344172
                else:
                    var22 = 0.084782146
    else:
        if input[7] < 329.0:
            if input[30] < 14.0:
                if input[12] < 0.19414414:
                    if input[5] < 1883.0:
                        var22 = 0.08406196
                    else:
                        var22 = 0.0337439
                else:
                    var22 = 0.085387625
            else:
                if input[11] < 0.24438202:
                    var22 = 0.08635973
                else:
                    var22 = 0.08519885
        else:
            if input[30] < 15.0:
                if input[12] < 0.21534973:
                    var22 = 0.08581249
                else:
                    if input[15] < 30.0:
                        var22 = 0.08638429
                    else:
                        var22 = 0.087554656
            else:
                if input[7] < 765.0:
                    if input[12] < 0.18503119:
                        var22 = 0.08662278
                    else:
                        var22 = 0.087673336
                else:
                    var22 = 0.088380545
    if input[7] < 155.0:
        if input[7] < 73.0:
            if input[7] < 44.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var23 = 0.070666075
                    else:
                        var23 = 0.029651647
                else:
                    var23 = 0.075637095
            else:
                if input[30] < 13.0:
                    var23 = 0.07838773
                else:
                    var23 = 0.08000518
        else:
            if input[30] < 14.0:
                if input[7] < 104.0:
                    var23 = 0.08032661
                else:
                    if input[12] < 0.15955351:
                        var23 = 0.08085343
                    else:
                        var23 = 0.08233307
            else:
                if input[7] < 110.0:
                    var23 = 0.082080774
                else:
                    var23 = 0.083492
    else:
        if input[7] < 347.0:
            if input[30] < 15.0:
                if input[12] < 0.20240137:
                    if input[11] < 0.34256172:
                        var23 = 0.083078094
                    else:
                        var23 = 0.07930241
                else:
                    var23 = 0.08432223
            else:
                if input[12] < 0.1473772:
                    var23 = 0.083783604
                else:
                    var23 = 0.08524219
        else:
            if input[30] < 15.0:
                if input[12] < 0.21595487:
                    var23 = 0.08459346
                else:
                    if input[15] < 30.0:
                        var23 = 0.085166015
                    else:
                        var23 = 0.086430125
            else:
                if input[12] < 0.18503119:
                    var23 = 0.08575267
                else:
                    if input[7] < 819.0:
                        var23 = 0.08661805
                    else:
                        var23 = 0.08756732
    if input[7] < 155.0:
        if input[7] < 79.0:
            if input[7] < 44.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var24 = 0.06852271
                    else:
                        var24 = 0.02804229
                else:
                    var24 = 0.073723674
            else:
                if input[30] < 12.0:
                    var24 = 0.0766764
                else:
                    var24 = 0.07843652
        else:
            if input[30] < 13.0:
                if input[7] < 106.0:
                    if input[6] < 470.0:
                        var24 = 0.078726724
                    else:
                        var24 = 0.04475728
                else:
                    if input[12] < 0.15883978:
                        var24 = 0.07897915
                    else:
                        var24 = 0.08070684
            else:
                if input[7] < 110.0:
                    var24 = 0.080570705
                else:
                    var24 = 0.08193248
    else:
        if input[7] < 347.0:
            if input[30] < 13.0:
                if input[12] < 0.19354838:
                    if input[5] < 1883.0:
                        var24 = 0.08097955
                    else:
                        var24 = 0.028469948
                else:
                    if input[6] < 570.0:
                        var24 = 0.08259719
                    else:
                        var24 = 0.03234353
            else:
                if input[12] < 0.1473772:
                    var24 = 0.08218008
                else:
                    if input[7] < 205.0:
                        var24 = 0.083007485
                    else:
                        var24 = 0.08399435
        else:
            if input[30] < 14.0:
                if input[12] < 0.20295984:
                    var24 = 0.08290289
                else:
                    if input[15] < 31.0:
                        var24 = 0.08381956
                    else:
                        var24 = 0.085036166
            else:
                if input[12] < 0.19248678:
                    var24 = 0.084442146
                else:
                    if input[7] < 819.0:
                        var24 = 0.08536812
                    else:
                        var24 = 0.08636927
    if input[7] < 155.0:
        if input[7] < 71.0:
            if input[7] < 38.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var25 = 0.06629523
                    else:
                        var25 = 0.026497269
                else:
                    var25 = 0.0705778
            else:
                if input[7] < 50.0:
                    if input[10] < 0.11857708:
                        var25 = 0.020157108
                    else:
                        var25 = 0.0733918
                else:
                    if input[30] < 11.0:
                        var25 = 0.07431471
                    else:
                        var25 = 0.076402925
        else:
            if input[7] < 106.0:
                if input[30] < 13.0:
                    if input[6] < 470.0:
                        var25 = 0.07677417
                    else:
                        var25 = 0.042711474
                else:
                    if input[12] < 0.13910761:
                        var25 = 0.07708009
                    else:
                        var25 = 0.07914309
            else:
                if input[30] < 14.0:
                    if input[12] < 0.16666667:
                        var25 = 0.07771206
                    else:
                        var25 = 0.0792822
                else:
                    var25 = 0.08046015
    else:
        if input[7] < 319.0:
            if input[30] < 14.0:
                if input[12] < 0.15883978:
                    if input[5] < 107.0:
                        var25 = 0.021031925
                    else:
                        var25 = 0.07879865
                else:
                    if input[11] < 0.27228683:
                        var25 = 0.08103945
                    else:
                        var25 = 0.07886418
            else:
                if input[12] < 0.14899713:
                    var25 = 0.08066841
                else:
                    if input[11] < 0.25531915:
                        var25 = 0.08249371
                    else:
                        var25 = 0.08111768
        else:
            if input[30] < 15.0:
                if input[12] < 0.20056497:
                    if input[5] < 80.0:
                        var25 = 0.030888034
                    else:
                        var25 = 0.08150564
                else:
                    if input[15] < 31.0:
                        var25 = 0.08248057
                    else:
                        var25 = 0.08380551
            else:
                if input[7] < 765.0:
                    if input[12] < 0.18503119:
                        var25 = 0.08271096
                    else:
                        var25 = 0.08399036
                else:
                    var25 = 0.08491073
    if input[7] < 155.0:
        if input[7] < 79.0:
            if input[7] < 46.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var26 = 0.063990615
                    else:
                        var26 = 0.025016908
                else:
                    if input[10] < 0.11857708:
                        var26 = 0.019188274
                    else:
                        var26 = 0.06993963
            else:
                if input[30] < 16.0:
                    if input[7] < 59.0:
                        var26 = 0.07232796
                    else:
                        var26 = 0.07415713
                else:
                    var26 = 0.075941056
        else:
            if input[30] < 13.0:
                if input[7] < 106.0:
                    if input[10] < 0.3962926:
                        var26 = 0.07514909
                    else:
                        var26 = 0.03814724
                else:
                    if input[12] < 0.14356436:
                        var26 = 0.07496902
                    else:
                        var26 = 0.07726167
            else:
                if input[7] < 110.0:
                    if input[12] < 0.1418919:
                        var26 = 0.07567753
                    else:
                        var26 = 0.07774923
                else:
                    var26 = 0.07875213
    else:
        if input[7] < 347.0:
            if input[30] < 15.0:
                if input[12] < 0.20240137:
                    if input[11] < 0.29132232:
                        var26 = 0.078526
                    else:
                        var26 = 0.07628469
                else:
                    var26 = 0.079897024
            else:
                if input[11] < 0.25804585:
                    if input[7] < 203.0:
                        var26 = 0.08011068
                    else:
                        var26 = 0.08142334
                else:
                    var26 = 0.07923465
        else:
            if input[30] < 14.0:
                if input[12] < 0.20295984:
                    var26 = 0.07984664
                else:
                    if input[15] < 31.0:
                        var26 = 0.080892414
                    else:
                        var26 = 0.082284175
            else:
                if input[12] < 0.20644216:
                    if input[12] < 0.12776025:
                        var26 = 0.08009644
                    else:
                        var26 = 0.08200782
                else:
                    if input[7] < 990.0:
                        var26 = 0.08285582
                    else:
                        var26 = 0.0840154
    if input[7] < 155.0:
        if input[7] < 79.0:
            if input[7] < 46.0:
                if input[7] < 34.0:
                    if input[13] < 0.46285716:
                        var27 = 0.06358605
                    else:
                        var27 = 0.023601128
                else:
                    if input[10] < 0.11857708:
                        var27 = 0.018262513
                    else:
                        var27 = 0.06836867
            else:
                if input[30] < 11.0:
                    if input[29] < 325.0:
                        var27 = 0.07053807
                    else:
                        var27 = 0.03425168
                else:
                    if input[6] < 833.0:
                        var27 = 0.07273219
                    else:
                        var27 = 0.027420191
        else:
            if input[30] < 12.0:
                if input[7] < 119.0:
                    if input[6] < 374.0:
                        var27 = 0.07328587
                    else:
                        var27 = 0.06048397
                else:
                    if input[10] < 0.07663783:
                        var27 = 0.022706129
                    else:
                        var27 = 0.07512596
            else:
                if input[7] < 110.0:
                    if input[12] < 0.14443277:
                        var27 = 0.07363328
                    else:
                        var27 = 0.07576981
                else:
                    var27 = 0.076877914
    else:
        if input[7] < 319.0:
            if input[30] < 14.0:
                if input[12] < 0.16210526:
                    if input[5] < 107.0:
                        var27 = 0.016336996
                    else:
                        var27 = 0.07530668
                else:
                    if input[11] < 0.27228683:
                        var27 = 0.07776188
                    else:
                        var27 = 0.075296454
            else:
                if input[12] < 0.14899713:
                    if input[10] < 0.13926017:
                        var27 = 0.07081293
                    else:
                        var27 = 0.07744857
                else:
                    if input[11] < 0.25531915:
                        var27 = 0.079389825
                    else:
                        var27 = 0.07783457
        else:
            if input[30] < 15.0:
                if input[12] < 0.20056497:
                    if input[5] < 80.0:
                        var27 = 0.025963858
                    else:
                        var27 = 0.07826334
                else:
                    if input[15] < 31.0:
                        var27 = 0.07937048
                    else:
                        var27 = 0.08087742
            else:
                if input[7] < 765.0:
                    if input[12] < 0.185567:
                        var27 = 0.079631574
                    else:
                        var27 = 0.0810938
                else:
                    var27 = 0.08215099
    if input[7] < 155.0:
        if input[7] < 73.0:
            if input[7] < 41.0:
                if input[7] < 29.0:
                    if input[13] < 0.45728898:
                        var28 = 0.0591042
                    else:
                        var28 = 0.02224945
                else:
                    if input[11] < 0.36167213:
                        var28 = 0.06469386
                    else:
                        var28 = 0.046659384
            else:
                if input[30] < 13.0:
                    if input[12] < 0.13622755:
                        var28 = 0.06620995
                    else:
                        var28 = 0.068981305
                else:
                    if input[12] < 0.11165048:
                        var28 = 0.06768212
                    else:
                        var28 = 0.0711549
        else:
            if input[30] < 14.0:
                if input[7] < 102.0:
                    if input[11] < 0.29132232:
                        var28 = 0.071324505
                    else:
                        var28 = 0.06698648
                else:
                    if input[12] < 0.15820895:
                        var28 = 0.07159935
                    else:
                        var28 = 0.073740415
            else:
                if input[7] < 110.0:
                    if input[6] < 470.0:
                        var28 = 0.07353071
                    else:
                        var28 = 0.061230917
                else:
                    var28 = 0.07533641
    else:
        if input[7] < 329.0:
            if input[30] < 15.0:
                if input[12] < 0.19476268:
                    if input[11] < 0.34256172:
                        var28 = 0.07457057
                    else:
                        var28 = 0.06908573
                else:
                    if input[30] < 11.0:
                        var28 = 0.07527217
                    else:
                        var28 = 0.07672752
            else:
                if input[11] < 0.25906184:
                    if input[7] < 203.0:
                        var28 = 0.07667662
                    else:
                        var28 = 0.07813527
                else:
                    if input[0] < 647.0:
                        var28 = 0.030907622
                    else:
                        var28 = 0.0755882
        else:
            if input[30] < 15.0:
                if input[12] < 0.21534973:
                    if input[5] < 80.0:
                        var28 = 0.024749158
                    else:
                        var28 = 0.076736525
                else:
                    if input[15] < 30.0:
                        var28 = 0.07759326
                    else:
                        var28 = 0.079369634
            else:
                if input[7] < 765.0:
                    if input[12] < 0.18503119:
                        var28 = 0.07793325
                    else:
                        var28 = 0.079532735
                else:
                    var28 = 0.080622874
    if input[7] < 194.0:
        if input[7] < 89.0:
            if input[7] < 50.0:
                if input[7] < 34.0:
                    if input[13] < 0.46285716:
                        var29 = 0.058722295
                    else:
                        var29 = 0.020961035
                else:
                    if input[10] < 0.11857708:
                        var29 = 0.013908098
                    else:
                        var29 = 0.064326316
            else:
                if input[30] < 11.0:
                    if input[12] < 0.13118812:
                        var29 = 0.063084446
                    else:
                        var29 = 0.06702234
                else:
                    if input[30] < 18.0:
                        var29 = 0.068869255
                    else:
                        var29 = 0.071501754
        else:
            if input[30] < 13.0:
                if input[12] < 0.15883978:
                    if input[5] < 61.0:
                        var29 = 0.021321272
                    else:
                        var29 = 0.0690201
                else:
                    if input[7] < 128.0:
                        var29 = 0.07054856
                    else:
                        var29 = 0.07243207
            else:
                if input[12] < 0.16335227:
                    if input[7] < 125.0:
                        var29 = 0.07097436
                    else:
                        var29 = 0.07282022
                else:
                    if input[30] < 17.0:
                        var29 = 0.07332958
                    else:
                        var29 = 0.07481807
    else:
        if input[7] < 458.0:
            if input[30] < 15.0:
                if input[11] < 0.2893082:
                    if input[12] < 0.2:
                        var29 = 0.07382938
                    else:
                        var29 = 0.075292915
                else:
                    if input[0] < 7051.0:
                        var29 = 0.07118569
                    else:
                        var29 = 0.020536294
            else:
                if input[11] < 0.25804585:
                    if input[12] < 0.1300813:
                        var29 = 0.07416382
                    else:
                        var29 = 0.07672923
                else:
                    var29 = 0.07443973
        else:
            if input[30] < 14.0:
                if input[12] < 0.22401847:
                    var29 = 0.075100146
                else:
                    if input[11] < 0.25906184:
                        var29 = 0.07734863
                    else:
                        var29 = 0.07261249
            else:
                if input[12] < 0.19248678:
                    var29 = 0.0769313
                else:
                    if input[11] < 0.22365038:
                        var29 = 0.07908998
                    else:
                        var29 = 0.07770138
    if input[7] < 194.0:
        if input[7] < 89.0:
            if input[7] < 50.0:
                if input[7] < 34.0:
                    if input[13] < 0.46285716:
                        var30 = 0.05622935
                    else:
                        var30 = 0.019734746
                else:
                    if input[10] < 0.11857708:
                        var30 = 0.013225496
                    else:
                        var30 = 0.061957177
            else:
                if input[30] < 11.0:
                    if input[12] < 0.13118812:
                        var30 = 0.060685057
                    else:
                        var30 = 0.06473718
                else:
                    if input[30] < 18.0:
                        var30 = 0.066650055
                    else:
                        var30 = 0.06939122
        else:
            if input[30] < 13.0:
                if input[12] < 0.15883978:
                    if input[5] < 61.0:
                        var30 = 0.020077435
                    else:
                        var30 = 0.06680697
                else:
                    if input[7] < 128.0:
                        var30 = 0.06839622
                    else:
                        var30 = 0.07036147
            else:
                if input[12] < 0.16335227:
                    if input[7] < 125.0:
                        var30 = 0.06884011
                    else:
                        var30 = 0.07076755
                else:
                    if input[30] < 17.0:
                        var30 = 0.071300566
                    else:
                        var30 = 0.07286205
    else:
        if input[7] < 458.0:
            if input[30] < 13.0:
                if input[12] < 0.19952267:
                    if input[8] < 259.0:
                        var30 = 0.024448706
                    else:
                        var30 = 0.070800655
                else:
                    var30 = 0.07291033
            else:
                if input[11] < 0.25622255:
                    if input[7] < 301.0:
                        var30 = 0.073864274
                    else:
                        var30 = 0.07507645
                else:
                    if input[35] < 17.352804:
                        var30 = 0.031862818
                    else:
                        var30 = 0.07229347
        else:
            if input[30] < 14.0:
                if input[12] < 0.22401847:
                    var30 = 0.073158495
                else:
                    if input[11] < 0.25906184:
                        var30 = 0.07552731
                    else:
                        var30 = 0.07055458
            else:
                if input[12] < 0.19248678:
                    if input[12] < 0.12776025:
                        var30 = 0.072973125
                    else:
                        var30 = 0.07544656
                else:
                    if input[11] < 0.22365038:
                        var30 = 0.07736916
                    else:
                        var30 = 0.07590004
    if input[7] < 189.0:
        if input[7] < 89.0:
            if input[7] < 50.0:
                if input[7] < 34.0:
                    if input[35] < 17.238165:
                        var31 = 0.03754179
                    else:
                        var31 = 0.053940494
                else:
                    if input[10] < 0.11857708:
                        var31 = 0.012575218
                    else:
                        var31 = 0.059526723
            else:
                if input[30] < 12.0:
                    if input[12] < 0.14285715:
                        var31 = 0.059822287
                    else:
                        var31 = 0.063032396
                else:
                    if input[12] < 0.17428088:
                        var31 = 0.06424368
                    else:
                        var31 = 0.06633553
        else:
            if input[30] < 14.0:
                if input[12] < 0.15820895:
                    if input[5] < 61.0:
                        var31 = 0.018894773
                    else:
                        var31 = 0.064812176
                else:
                    if input[7] < 119.0:
                        var31 = 0.06614529
                    else:
                        var31 = 0.06818448
            else:
                if input[12] < 0.15197569:
                    if input[7] < 111.0:
                        var31 = 0.06581887
                    else:
                        var31 = 0.06844338
                else:
                    if input[30] < 17.0:
                        var31 = 0.06911332
                    else:
                        var31 = 0.07072523
    else:
        if input[7] < 458.0:
            if input[30] < 13.0:
                if input[12] < 0.19952267:
                    if input[11] < 0.38214287:
                        var31 = 0.06863412
                    else:
                        var31 = 0.052896775
                else:
                    if input[5] < 102.0:
                        var31 = 0.0664823
                    else:
                        var31 = 0.07098846
            else:
                if input[11] < 0.25714287:
                    if input[7] < 245.0:
                        var31 = 0.07134331
                    else:
                        var31 = 0.07285498
                else:
                    if input[35] < 17.352804:
                        var31 = 0.040409412
                    else:
                        var31 = 0.07013035
        else:
            if input[30] < 14.0:
                if input[12] < 0.19414414:
                    var31 = 0.07050926
                else:
                    if input[11] < 0.260095:
                        var31 = 0.073278226
                    else:
                        var31 = 0.0698139
            else:
                if input[12] < 0.19248678:
                    if input[12] < 0.12776025:
                        var31 = 0.07092901
                    else:
                        var31 = 0.07352272
                else:
                    if input[11] < 0.22365038:
                        var31 = 0.07554885
                    else:
                        var31 = 0.074000075
    if input[7] < 164.0:
        if input[7] < 79.0:
            if input[7] < 44.0:
                if input[7] < 29.0:
                    if input[15] < 14.0:
                        var32 = 0.018790375
                    else:
                        var32 = 0.048808604
                else:
                    if input[10] < 0.16041848:
                        var32 = 0.04361366
                    else:
                        var32 = 0.055605598
            else:
                if input[30] < 16.0:
                    if input[7] < 58.0:
                        var32 = 0.058250755
                    else:
                        var32 = 0.06088992
                else:
                    if input[12] < 0.115189336:
                        var32 = 0.05972987
                    else:
                        var32 = 0.06401579
        else:
            if input[30] < 15.0:
                if input[7] < 106.0:
                    if input[11] < 0.25804585:
                        var32 = 0.06306707
                    else:
                        var32 = 0.059991974
                else:
                    if input[10] < 0.37548056:
                        var32 = 0.06509545
                    else:
                        var32 = 0.04747915
            else:
                if input[12] < 0.16783217:
                    if input[10] < 0.1463964:
                        var32 = 0.05791818
                    else:
                        var32 = 0.065746
                else:
                    var32 = 0.06757678
    else:
        if input[7] < 358.0:
            if input[30] < 13.0:
                if input[12] < 0.19354838:
                    if input[5] < 1883.0:
                        var32 = 0.065442346
                    else:
                        var32 = 0.0018318594
                else:
                    if input[5] < 102.0:
                        var32 = 0.06314737
                    else:
                        var32 = 0.0682578
            else:
                if input[11] < 0.24438202:
                    if input[7] < 222.0:
                        var32 = 0.0688345
                    else:
                        var32 = 0.070440724
                else:
                    if input[12] < 0.09598741:
                        var32 = 0.06236977
                    else:
                        var32 = 0.06787258
        else:
            if input[30] < 15.0:
                if input[12] < 0.21595487:
                    if input[12] < 0.13622755:
                        var32 = 0.066126816
                    else:
                        var32 = 0.06922937
                else:
                    if input[15] < 30.0:
                        var32 = 0.06972258
                    else:
                        var32 = 0.07206582
            else:
                if input[12] < 0.18503119:
                    if input[12] < 0.12776025:
                        var32 = 0.06860577
                    else:
                        var32 = 0.07129086
                else:
                    if input[7] < 819.0:
                        var32 = 0.07235571
                    else:
                        var32 = 0.07405339
    if input[7] < 194.0:
        if input[7] < 89.0:
            if input[7] < 50.0:
                if input[7] < 34.0:
                    if input[35] < 17.238165:
                        var33 = 0.032202527
                    else:
                        var33 = 0.048791837
                else:
                    if input[10] < 0.11857708:
                        var33 = 0.00907581
                    else:
                        var33 = 0.05452863
            else:
                if input[30] < 11.0:
                    if input[5] < 343.0:
                        var33 = 0.056757655
                    else:
                        var33 = 0.01604676
                else:
                    if input[30] < 18.0:
                        var33 = 0.059555717
                    else:
                        var33 = 0.062675804
        else:
            if input[30] < 13.0:
                if input[12] < 0.15883978:
                    if input[5] < 61.0:
                        var33 = 0.014142767
                    else:
                        var33 = 0.059619214
                else:
                    if input[7] < 128.0:
                        var33 = 0.061438102
                    else:
                        var33 = 0.063637055
            else:
                if input[12] < 0.16335227:
                    if input[12] < 0.09598741:
                        var33 = 0.05972622
                    else:
                        var33 = 0.06360297
                else:
                    if input[30] < 17.0:
                        var33 = 0.064706296
                    else:
                        var33 = 0.06647256
    else:
        if input[7] < 549.0:
            if input[30] < 15.0:
                if input[11] < 0.2893082:
                    if input[12] < 0.19887955:
                        var33 = 0.06535538
                    else:
                        var33 = 0.06712874
                else:
                    if input[8] < 221.0:
                        var33 = 0.02031722
                    else:
                        var33 = 0.06240527
            else:
                if input[12] < 0.17199096:
                    if input[12] < 0.119382024:
                        var33 = 0.06416757
                    else:
                        var33 = 0.06731289
                else:
                    if input[7] < 301.0:
                        var33 = 0.06807416
                    else:
                        var33 = 0.06963304
        else:
            if input[30] < 16.0:
                if input[12] < 0.16783217:
                    if input[10] < 0.10353011:
                        var33 = 0.045070853
                    else:
                        var33 = 0.06575977
                else:
                    if input[22] < 5.385421:
                        var33 = 0.06809596
                    else:
                        var33 = 0.07022168
            else:
                if input[11] < 0.26459855:
                    if input[12] < 0.18401015:
                        var33 = 0.070071176
                    else:
                        var33 = 0.071950085
                else:
                    if input[16] < 27.717241:
                        var33 = 0.01962035
                    else:
                        var33 = 0.06884682
    if input[7] < 205.0:
        if input[7] < 89.0:
            if input[7] < 46.0:
                if input[7] < 29.0:
                    if input[30] < 10.0:
                        var34 = 0.03768922
                    else:
                        var34 = 0.045863543
                else:
                    if input[10] < 0.14310052:
                        var34 = 0.033790167
                    else:
                        var34 = 0.05078761
            else:
                if input[30] < 11.0:
                    if input[12] < 0.19414414:
                        var34 = 0.0527681
                    else:
                        var34 = 0.056033876
                else:
                    if input[7] < 63.0:
                        var34 = 0.055374563
                    else:
                        var34 = 0.058155995
        else:
            if input[30] < 13.0:
                if input[12] < 0.15883978:
                    if input[5] < 61.0:
                        var34 = 0.013273402
                    else:
                        var34 = 0.057288945
                else:
                    if input[7] < 128.0:
                        var34 = 0.058995314
                    else:
                        var34 = 0.061368097
            else:
                if input[12] < 0.14516129:
                    if input[7] < 111.0:
                        var34 = 0.05787869
                    else:
                        var34 = 0.061029293
                else:
                    if input[7] < 125.0:
                        var34 = 0.061463606
                    else:
                        var34 = 0.0635688
    else:
        if input[7] < 549.0:
            if input[30] < 15.0:
                if input[11] < 0.29132232:
                    if input[12] < 0.20465116:
                        var34 = 0.063196294
                    else:
                        var34 = 0.06502558
                else:
                    if input[0] < 7051.0:
                        var34 = 0.05994625
                    else:
                        var34 = 0.0063986266
            else:
                if input[12] < 0.17943697:
                    if input[12] < 0.119382024:
                        var34 = 0.062134165
                    else:
                        var34 = 0.065200455
                else:
                    if input[11] < 0.25714287:
                        var34 = 0.067244075
                    else:
                        var34 = 0.06435429
        else:
            if input[30] < 12.0:
                if input[11] < 0.3178114:
                    if input[5] < 138.0:
                        var34 = 0.029104197
                    else:
                        var34 = 0.06553623
                else:
                    if input[26] < 27.391703:
                        var34 = 0.055266965
                    else:
                        var34 = 0.012963136
            else:
                if input[12] < 0.19178082:
                    if input[30] < 16.0:
                        var34 = 0.064961195
                    else:
                        var34 = 0.067691706
                else:
                    if input[30] < 17.0:
                        var34 = 0.06835961
                    else:
                        var34 = 0.069981925
    if input[7] < 205.0:
        if input[7] < 89.0:
            if input[7] < 50.0:
                if input[7] < 34.0:
                    if input[12] < 0.14356436:
                        var35 = 0.040833555
                    else:
                        var35 = 0.046816602
                else:
                    if input[13] < 0.47155812:
                        var35 = 0.04945038
                    else:
                        var35 = 0.020611517
            else:
                if input[30] < 12.0:
                    if input[12] < 0.14285715:
                        var35 = 0.049336206
                    else:
                        var35 = 0.053157885
                else:
                    if input[12] < 0.17428088:
                        var35 = 0.054370146
                    else:
                        var35 = 0.056917127
        else:
            if input[30] < 12.0:
                if input[12] < 0.15883978:
                    if input[10] < 0.10353011:
                        var35 = 0.029495029
                    else:
                        var35 = 0.05419631
                else:
                    if input[7] < 125.0:
                        var35 = 0.056029137
                    else:
                        var35 = 0.058536
            else:
                if input[12] < 0.14443277:
                    if input[7] < 110.0:
                        var35 = 0.05498714
                    else:
                        var35 = 0.05828721
                else:
                    if input[7] < 125.0:
                        var35 = 0.058854457
                    else:
                        var35 = 0.06097244
    else:
        if input[7] < 549.0:
            if input[30] < 13.0:
                if input[12] < 0.124279834:
                    if input[5] < 491.0:
                        var35 = 0.045422908
                    else:
                        var35 = 0.056163788
                else:
                    if input[11] < 0.28:
                        var35 = 0.061555594
                    else:
                        var35 = 0.05829623
            else:
                if input[12] < 0.20179372:
                    if input[11] < 0.28440368:
                        var35 = 0.06289519
                    else:
                        var35 = 0.060270198
                else:
                    if input[11] < 0.25714287:
                        var35 = 0.06481157
                    else:
                        var35 = 0.061596014
        else:
            if input[30] < 12.0:
                if input[11] < 0.32142857:
                    if input[5] < 138.0:
                        var35 = 0.02731487
                    else:
                        var35 = 0.0631822
                else:
                    if input[26] < 27.391703:
                        var35 = 0.05200248
                    else:
                        var35 = 0.012160025
            else:
                if input[12] < 0.19178082:
                    if input[30] < 16.0:
                        var35 = 0.062610805
                    else:
                        var35 = 0.06542971
                else:
                    if input[30] < 17.0:
                        var35 = 0.06612135
                    else:
                        var35 = 0.0678063
    if input[7] < 205.0:
        if input[7] < 89.0:
            if input[7] < 58.0:
                if input[7] < 38.0:
                    if input[20] < 10.793282:
                        var36 = 0.039368633
                    else:
                        var36 = 0.045010787
                else:
                    if input[22] < 4.671156:
                        var36 = 0.04671466
                    else:
                        var36 = 0.04980336
            else:
                if input[30] < 12.0:
                    if input[5] < 373.0:
                        var36 = 0.050290722
                    else:
                        var36 = 0.018792504
                else:
                    if input[12] < 0.17428088:
                        var36 = 0.05217749
                    else:
                        var36 = 0.054821707
        else:
            if input[30] < 15.0:
                if input[12] < 0.15625:
                    if input[11] < 0.115555555:
                        var36 = 0.040664103
                    else:
                        var36 = 0.052997787
                else:
                    if input[7] < 119.0:
                        var36 = 0.054062545
                    else:
                        var36 = 0.05669829
            else:
                if input[12] < 0.16535832:
                    if input[10] < 0.14970563:
                        var36 = 0.04749067
                    else:
                        var36 = 0.056807894
                else:
                    if input[7] < 128.0:
                        var36 = 0.057475537
                    else:
                        var36 = 0.059421934
    else:
        if input[7] < 458.0:
            if input[30] < 16.0:
                if input[12] < 0.1971831:
                    if input[30] < 11.0:
                        var36 = 0.055313736
                    else:
                        var36 = 0.058402844
                else:
                    if input[30] < 12.0:
                        var36 = 0.058897473
                    else:
                        var36 = 0.060939413
            else:
                if input[11] < 0.25804585:
                    if input[10] < 0.35:
                        var36 = 0.06225602
                    else:
                        var36 = 0.056605678
                else:
                    if input[12] < 0.063964844:
                        var36 = 0.0395259
                    else:
                        var36 = 0.058945794
        else:
            if input[30] < 13.0:
                if input[12] < 0.22401847:
                    if input[12] < 0.13622755:
                        var36 = 0.054914713
                    else:
                        var36 = 0.059682693
                else:
                    if input[11] < 0.25804585:
                        var36 = 0.062409826
                    else:
                        var36 = 0.05551071
            else:
                if input[12] < 0.19248678:
                    if input[22] < 6.441144:
                        var36 = 0.060638595
                    else:
                        var36 = 0.062994204
                else:
                    if input[7] < 990.0:
                        var36 = 0.0638098
                    else:
                        var36 = 0.065659635
    if input[7] < 155.0:
        if input[7] < 64.0:
            if input[7] < 38.0:
                if input[16] < 18.790983:
                    if input[12] < 0.13118812:
                        var37 = 0.026174206
                    else:
                        var37 = 0.039226588
                else:
                    if input[19] < 43.5507:
                        var37 = 0.018295381
                    else:
                        var37 = 0.042108793
            else:
                if input[30] < 11.0:
                    if input[12] < 0.19067797:
                        var37 = 0.04253648
                    else:
                        var37 = 0.04729209
                else:
                    if input[12] < 0.11165048:
                        var37 = 0.04366484
                    else:
                        var37 = 0.048020516
        else:
            if input[7] < 106.0:
                if input[30] < 15.0:
                    if input[12] < 0.13118812:
                        var37 = 0.04612897
                    else:
                        var37 = 0.050073322
                else:
                    if input[12] < 0.14899713:
                        var37 = 0.05061545
                    else:
                        var37 = 0.053644568
            else:
                if input[30] < 11.0:
                    if input[10] < 0.35634327:
                        var37 = 0.050951578
                    else:
                        var37 = 0.02917705
                else:
                    if input[30] < 16.0:
                        var37 = 0.053507186
                    else:
                        var37 = 0.0555932
    else:
        if input[7] < 319.0:
            if input[30] < 15.0:
                if input[11] < 0.2734694:
                    if input[12] < 0.19476268:
                        var37 = 0.054003067
                    else:
                        var37 = 0.0564601
                else:
                    if input[11] < 0.34256172:
                        var37 = 0.052007314
                    else:
                        var37 = 0.044350944
            else:
                if input[12] < 0.14899713:
                    if input[10] < 0.13652053:
                        var37 = 0.040961947
                    else:
                        var37 = 0.055330236
                else:
                    if input[30] < 18.0:
                        var37 = 0.05752824
                    else:
                        var37 = 0.059396844
        else:
            if input[30] < 16.0:
                if input[12] < 0.19128329:
                    if input[30] < 11.0:
                        var37 = 0.053843122
                    else:
                        var37 = 0.05718384
                else:
                    if input[22] < 5.1931043:
                        var37 = 0.057988282
                    else:
                        var37 = 0.06045534
            else:
                if input[7] < 765.0:
                    if input[11] < 0.25906184:
                        var37 = 0.06089611
                    else:
                        var37 = 0.05789574
                else:
                    if input[11] < 0.30646765:
                        var37 = 0.063232645
                    else:
                        var37 = 0.05692658
    if input[7] < 205.0:
        if input[7] < 84.0:
            if input[7] < 46.0:
                if input[7] < 29.0:
                    if input[30] < 10.0:
                        var38 = 0.027309993
                    else:
                        var38 = 0.03602682
                else:
                    if input[30] < 13.0:
                        var38 = 0.039260145
                    else:
                        var38 = 0.04327878
            else:
                if input[30] < 16.0:
                    if input[11] < 0.27471566:
                        var38 = 0.045604583
                    else:
                        var38 = 0.041286755
                else:
                    if input[12] < 0.11165048:
                        var38 = 0.044149756
                    else:
                        var38 = 0.0498488
        else:
            if input[30] < 11.0:
                if input[12] < 0.16465864:
                    if input[0] < 526.0:
                        var38 = -0.02352186
                    else:
                        var38 = 0.04562011
                else:
                    if input[6] < 387.0:
                        var38 = 0.04928168
                    else:
                        var38 = -0.018126694
            else:
                if input[7] < 128.0:
                    if input[8] < 581.0:
                        var38 = 0.05045522
                    else:
                        var38 = 0.037072454
                else:
                    if input[11] < 0.3178114:
                        var38 = 0.053084295
                    else:
                        var38 = 0.046821974
    else:
        if input[7] < 557.0:
            if input[30] < 15.0:
                if input[11] < 0.29132232:
                    if input[12] < 0.21780303:
                        var38 = 0.053483527
                    else:
                        var38 = 0.055467486
                else:
                    if input[8] < 2534.0:
                        var38 = 0.04959988
                    else:
                        var38 = 0.007964218
            else:
                if input[12] < 0.17943697:
                    if input[12] < 0.119382024:
                        var38 = 0.051879432
                    else:
                        var38 = 0.055450626
                else:
                    if input[11] < 0.25714287:
                        var38 = 0.057822414
                    else:
                        var38 = 0.054533422
        else:
            if input[30] < 12.0:
                if input[11] < 0.3178114:
                    if input[5] < 138.0:
                        var38 = 0.017918928
                    else:
                        var38 = 0.05584977
                else:
                    if input[22] < 6.2262416:
                        var38 = 0.044285275
                    else:
                        var38 = 0.0027041635
            else:
                if input[12] < 0.168435:
                    if input[30] < 19.0:
                        var38 = 0.05552889
                    else:
                        var38 = 0.06013426
                else:
                    if input[11] < 0.24930875:
                        var38 = 0.060079157
                    else:
                        var38 = 0.05732056
    if input[7] < 194.0:
        if input[7] < 79.0:
            if input[7] < 44.0:
                if input[7] < 29.0:
                    if input[15] < 14.0:
                        var39 = 0.00091426633
                    else:
                        var39 = 0.031399626
                else:
                    if input[10] < 0.16041848:
                        var39 = 0.02329143
                    else:
                        var39 = 0.037892237
            else:
                if input[30] < 16.0:
                    if input[12] < 0.12893553:
                        var39 = 0.039171092
                    else:
                        var39 = 0.04285602
                else:
                    if input[12] < 0.115189336:
                        var39 = 0.04156147
                    else:
                        var39 = 0.046906453
        else:
            if input[30] < 14.0:
                if input[12] < 0.1418919:
                    if input[11] < 0.088716626:
                        var39 = 0.004667513
                    else:
                        var39 = 0.043346506
                else:
                    if input[7] < 119.0:
                        var39 = 0.045692865
                    else:
                        var39 = 0.048476677
            else:
                if input[7] < 116.0:
                    if input[29] < 276.0:
                        var39 = 0.048253607
                    else:
                        var39 = 0.040563818
                else:
                    if input[11] < 0.29727095:
                        var39 = 0.05102378
                    else:
                        var39 = 0.045942854
    else:
        if input[7] < 427.0:
            if input[11] < 0.24074075:
                if input[30] < 11.0:
                    if input[35] < 17.770382:
                        var39 = 0.04634809
                    else:
                        var39 = 0.05086459
                else:
                    if input[30] < 18.0:
                        var39 = 0.053085882
                    else:
                        var39 = 0.05534575
            else:
                if input[30] < 13.0:
                    if input[11] < 0.38214287:
                        var39 = 0.04799318
                    else:
                        var39 = 0.026215006
                else:
                    if input[11] < 0.2893082:
                        var39 = 0.051923957
                    else:
                        var39 = 0.049145576
        else:
            if input[30] < 16.0:
                if input[12] < 0.20408164:
                    if input[12] < 0.080063626:
                        var39 = 0.033658873
                    else:
                        var39 = 0.052249085
                else:
                    if input[22] < 5.385421:
                        var39 = 0.053446364
                    else:
                        var39 = 0.056361664
            else:
                if input[7] < 839.0:
                    if input[12] < 0.20056497:
                        var39 = 0.05449715
                    else:
                        var39 = 0.05699749
                else:
                    if input[11] < 0.30646765:
                        var39 = 0.058636606
                    else:
                        var39 = 0.05150503
    if input[7] < 205.0:
        if input[7] < 89.0:
            if input[7] < 58.0:
                if input[7] < 38.0:
                    if input[20] < 10.793282:
                        var40 = 0.02971509
                    else:
                        var40 = 0.035280593
                else:
                    if input[10] < 0.1839934:
                        var40 = 0.032332048
                    else:
                        var40 = 0.03844116
            else:
                if input[30] < 12.0:
                    if input[5] < 373.0:
                        var40 = 0.040031504
                    else:
                        var40 = 0.0072183223
                else:
                    if input[8] < 615.0:
                        var40 = 0.043189492
                    else:
                        var40 = 0.013434418
        else:
            if input[30] < 11.0:
                if input[12] < 0.16210526:
                    if input[11] < 0.13968255:
                        var40 = 0.02937898
                    else:
                        var40 = 0.040903926
                else:
                    if input[6] < 387.0:
                        var40 = 0.044263203
                    else:
                        var40 = -0.018706447
            else:
                if input[12] < 0.14443277:
                    if input[12] < 0.09598741:
                        var40 = 0.04044453
                    else:
                        var40 = 0.04505432
                else:
                    if input[30] < 17.0:
                        var40 = 0.046836626
                    else:
                        var40 = 0.049323156
    else:
        if input[7] < 557.0:
            if input[30] < 16.0:
                if input[12] < 0.1971831:
                    if input[12] < 0.124279834:
                        var40 = 0.043951653
                    else:
                        var40 = 0.048185866
                else:
                    if input[30] < 12.0:
                        var40 = 0.048794597
                    else:
                        var40 = 0.051158514
            else:
                if input[11] < 0.25906184:
                    if input[10] < 0.3075:
                        var40 = 0.05276407
                    else:
                        var40 = 0.048761606
                else:
                    if input[12] < 0.063964844:
                        var40 = 0.02760082
                    else:
                        var40 = 0.049189467
        else:
            if input[30] < 12.0:
                if input[11] < 0.25:
                    if input[10] < 0.24009325:
                        var40 = 0.052533697
                    else:
                        var40 = 0.047862343
                else:
                    if input[20] < 17.262295:
                        var40 = 0.0378793
                    else:
                        var40 = 0.04779458
            else:
                if input[12] < 0.168435:
                    if input[30] < 19.0:
                        var40 = 0.050370194
                    else:
                        var40 = 0.055234976
                else:
                    if input[15] < 36.0:
                        var40 = 0.05352931
                    else:
                        var40 = 0.055685516
    if input[7] < 222.0:
        if input[7] < 104.0:
            if input[7] < 58.0:
                if input[7] < 38.0:
                    if input[16] < 18.382183:
                        var41 = 0.026271269
                    else:
                        var41 = 0.031954776
                else:
                    if input[6] < 84.0:
                        var41 = 0.03663367
                    else:
                        var41 = 0.032855462
            else:
                if input[30] < 12.0:
                    if input[6] < 399.0:
                        var41 = 0.038103517
                    else:
                        var41 = 0.006684655
                else:
                    if input[12] < 0.14899713:
                        var41 = 0.039044525
                    else:
                        var41 = 0.04222812
        else:
            if input[30] < 11.0:
                if input[10] < 0.33581847:
                    if input[11] < 0.21112256:
                        var41 = 0.042950347
                    else:
                        var41 = 0.039427724
                else:
                    if input[12] < 0.07342466:
                        var41 = -0.027898153
                    else:
                        var41 = 0.032506865
            else:
                if input[12] < 0.16335227:
                    if input[12] < 0.09598741:
                        var41 = 0.03876144
                    else:
                        var41 = 0.043567322
                else:
                    if input[30] < 17.0:
                        var41 = 0.044990003
                    else:
                        var41 = 0.04760701
    else:
        if input[7] < 703.0:
            if input[30] < 13.0:
                if input[12] < 0.1300813:
                    if input[10] < 0.16571428:
                        var41 = 0.02091475
                    else:
                        var41 = 0.040821623
                else:
                    if input[11] < 0.24857685:
                        var41 = 0.047046363
                    else:
                        var41 = 0.043976255
            else:
                if input[12] < 0.20179372:
                    if input[12] < 0.10803619:
                        var41 = 0.043351833
                    else:
                        var41 = 0.04802142
                else:
                    if input[11] < 0.24291939:
                        var41 = 0.05064976
                    else:
                        var41 = 0.047408722
        else:
            if input[11] < 0.25804585:
                if input[30] < 17.0:
                    if input[10] < 0.24390244:
                        var41 = 0.051840853
                    else:
                        var41 = 0.048230127
                else:
                    if input[10] < 0.37548056:
                        var41 = 0.053952683
                    else:
                        var41 = 0.03457617
            else:
                if input[19] < 177.12387:
                    if input[10] < 0.10353011:
                        var41 = 0.025979102
                    else:
                        var41 = -0.040199734
                else:
                    if input[15] < 37.0:
                        var41 = 0.04533007
                    else:
                        var41 = 0.05002156
    if input[7] < 164.0:
        if input[7] < 71.0:
            if input[7] < 41.0:
                if input[22] < 3.9122171:
                    if input[12] < 0.15049505:
                        var42 = 0.019415313
                    else:
                        var42 = 0.02951853
                else:
                    if input[8] < 197.0:
                        var42 = 0.030689314
                    else:
                        var42 = 0.014780971
            else:
                if input[30] < 16.0:
                    if input[12] < 0.1300813:
                        var42 = 0.03097938
                    else:
                        var42 = 0.034700125
                else:
                    if input[13] < 0.4256757:
                        var42 = 0.03875948
                    else:
                        var42 = 0.027614841
        else:
            if input[30] < 14.0:
                if input[12] < 0.1418919:
                    if input[11] < 0.14344262:
                        var42 = 0.02004533
                    else:
                        var42 = 0.035715263
                else:
                    if input[10] < 0.1549101:
                        var42 = 0.03498293
                    else:
                        var42 = 0.039658584
            else:
                if input[7] < 110.0:
                    if input[6] < 470.0:
                        var42 = 0.03995759
                    else:
                        var42 = 0.019107267
                else:
                    if input[6] < 305.0:
                        var42 = 0.042794302
                    else:
                        var42 = 0.038835
    else:
        if input[7] < 319.0:
            if input[30] < 16.0:
                if input[11] < 0.2785235:
                    if input[12] < 0.19476268:
                        var42 = 0.041446317
                    else:
                        var42 = 0.043970376
                else:
                    if input[26] < 176.9332:
                        var42 = 0.03801043
                    else:
                        var42 = -0.023591002
            else:
                if input[6] < 554.0:
                    if input[29] < 57.0:
                        var42 = 0.018482536
                    else:
                        var42 = 0.045830023
                else:
                    if input[11] < 0.3506606:
                        var42 = 0.040618293
                    else:
                        var42 = 0.025685156
        else:
            if input[30] < 16.0:
                if input[12] < 0.21595487:
                    if input[30] < 11.0:
                        var42 = 0.041437056
                    else:
                        var42 = 0.045039997
                else:
                    if input[15] < 30.0:
                        var42 = 0.045497447
                    else:
                        var42 = 0.048602708
            else:
                if input[7] < 765.0:
                    if input[11] < 0.22622779:
                        var42 = 0.048749126
                    else:
                        var42 = 0.046123005
                else:
                    if input[11] < 0.31177828:
                        var42 = 0.050921183
                    else:
                        var42 = 0.04279736
    if input[7] < 222.0:
        if input[7] < 104.0:
            if input[7] < 58.0:
                if input[22] < 4.7004967:
                    if input[12] < 0.13118812:
                        var43 = 0.022261534
                    else:
                        var43 = 0.02985457
                else:
                    if input[13] < 0.41038525:
                        var43 = 0.033365708
                    else:
                        var43 = 0.027514726
            else:
                if input[30] < 16.0:
                    if input[11] < 0.26088542:
                        var43 = 0.03492299
                    else:
                        var43 = 0.031031484
                else:
                    if input[12] < 0.11165048:
                        var43 = 0.03282324
                    else:
                        var43 = 0.038377132
        else:
            if input[30] < 11.0:
                if input[10] < 0.30397022:
                    if input[11] < 0.21176471:
                        var43 = 0.03836075
                    else:
                        var43 = 0.034511786
                else:
                    if input[20] < 17.784946:
                        var43 = 0.030359289
                    else:
                        var43 = -0.0077494713
            else:
                if input[12] < 0.16335227:
                    if input[35] < 17.880209:
                        var43 = 0.035883993
                    else:
                        var43 = 0.039022904
                else:
                    if input[30] < 18.0:
                        var43 = 0.04017675
                    else:
                        var43 = 0.043171015
    else:
        if input[15] < 35.0:
            if input[12] < 0.20056497:
                if input[12] < 0.124279834:
                    if input[12] < 0.063964844:
                        var43 = 0.010932337
                    else:
                        var43 = 0.03656756
                else:
                    if input[10] < 0.15306123:
                        var43 = 0.037004896
                    else:
                        var43 = 0.042066246
            else:
                if input[15] < 30.0:
                    if input[11] < 0.24857685:
                        var43 = 0.043071117
                    else:
                        var43 = 0.03856362
                else:
                    if input[11] < 0.25270757:
                        var43 = 0.04556712
                    else:
                        var43 = 0.0413951
        else:
            if input[12] < 0.17320575:
                if input[10] < 0.110275686:
                    if input[4] < 10162.0:
                        var43 = 0.033132877
                    else:
                        var43 = -0.00085026363
                else:
                    if input[12] < 0.12069428:
                        var43 = 0.040398862
                    else:
                        var43 = 0.04434163
            else:
                if input[11] < 0.22365038:
                    if input[30] < 17.0:
                        var43 = 0.046971392
                    else:
                        var43 = 0.048971426
                else:
                    if input[5] < 110.0:
                        var43 = 0.006242081
                    else:
                        var43 = 0.04522712
    if input[7] < 151.0:
        if input[7] < 64.0:
            if input[7] < 38.0:
                if input[20] < 10.793282:
                    if input[12] < 0.10969388:
                        var44 = 0.008109957
                    else:
                        var44 = 0.023681542
                else:
                    if input[8] < 197.0:
                        var44 = 0.027480489
                    else:
                        var44 = 0.00989714
            else:
                if input[30] < 11.0:
                    if input[12] < 0.19067797:
                        var44 = 0.025147809
                    else:
                        var44 = 0.030675748
                else:
                    if input[10] < 0.18523775:
                        var44 = 0.024157433
                    else:
                        var44 = 0.031021519
        else:
            if input[30] < 16.0:
                if input[11] < 0.2875817:
                    if input[12] < 0.14516129:
                        var44 = 0.031241227
                    else:
                        var44 = 0.03464524
                else:
                    if input[10] < 0.08773527:
                        var44 = -0.0012807929
                    else:
                        var44 = 0.028987262
            else:
                if input[7] < 98.0:
                    if input[13] < 0.4273577:
                        var44 = 0.035540257
                    else:
                        var44 = 0.024776198
                else:
                    if input[10] < 0.34461153:
                        var44 = 0.038183913
                    else:
                        var44 = 0.030027533
    else:
        if input[7] < 319.0:
            if input[30] < 16.0:
                if input[11] < 0.24074075:
                    if input[10] < 0.305761:
                        var44 = 0.038639303
                    else:
                        var44 = 0.033871572
                else:
                    if input[11] < 0.34256172:
                        var44 = 0.035413753
                    else:
                        var44 = 0.027306227
            else:
                if input[11] < 0.25906184:
                    if input[10] < 0.3008415:
                        var44 = 0.04121744
                    else:
                        var44 = 0.03781973
                else:
                    if input[12] < 0.080063626:
                        var44 = 0.024377314
                    else:
                        var44 = 0.037413843
        else:
            if input[30] < 13.0:
                if input[12] < 0.13622755:
                    if input[10] < 0.13926017:
                        var44 = 0.013318571
                    else:
                        var44 = 0.033809274
                else:
                    if input[11] < 0.3178114:
                        var44 = 0.040529586
                    else:
                        var44 = 0.031570192
            else:
                if input[12] < 0.20644216:
                    if input[22] < 6.441144:
                        var44 = 0.04024715
                    else:
                        var44 = 0.043006834
                else:
                    if input[15] < 35.0:
                        var44 = 0.043128267
                    else:
                        var44 = 0.04564519
    if input[7] < 222.0:
        if input[7] < 106.0:
            if input[7] < 58.0:
                if input[7] < 34.0:
                    if input[12] < 0.14356436:
                        var45 = 0.017778944
                    else:
                        var45 = 0.02530557
                else:
                    if input[30] < 15.0:
                        var45 = 0.025465429
                    else:
                        var45 = 0.030131584
            else:
                if input[30] < 12.0:
                    if input[10] < 0.11592958:
                        var45 = 0.01079971
                    else:
                        var45 = 0.028781597
                else:
                    if input[12] < 0.14899713:
                        var45 = 0.029541442
                    else:
                        var45 = 0.032852855
        else:
            if input[30] < 11.0:
                if input[10] < 0.30397022:
                    if input[10] < 0.1689441:
                        var45 = 0.028279675
                    else:
                        var45 = 0.03287038
                else:
                    if input[35] < 17.238165:
                        var45 = 0.008000428
                    else:
                        var45 = 0.026277963
            else:
                if input[12] < 0.20930232:
                    if input[30] < 16.0:
                        var45 = 0.033252794
                    else:
                        var45 = 0.03565337
                else:
                    if input[10] < 0.09894699:
                        var45 = 0.021795142
                    else:
                        var45 = 0.036908224
    else:
        if input[30] < 16.0:
            if input[12] < 0.1971831:
                if input[30] < 11.0:
                    if input[5] < 202.0:
                        var45 = 0.008775298
                    else:
                        var45 = 0.03307701
                else:
                    if input[29] < 198.0:
                        var45 = 0.027202472
                    else:
                        var45 = 0.03659766
            else:
                if input[15] < 30.0:
                    if input[11] < 0.24857685:
                        var45 = 0.037720192
                    else:
                        var45 = 0.033403393
                else:
                    if input[11] < 0.25270757:
                        var45 = 0.04074871
                    else:
                        var45 = 0.036681138
        else:
            if input[7] < 765.0:
                if input[11] < 0.26459855:
                    if input[12] < 0.20179372:
                        var45 = 0.038926557
                    else:
                        var45 = 0.04119062
                else:
                    if input[10] < 0.23641305:
                        var45 = 0.03696417
                    else:
                        var45 = 0.030606551
            else:
                if input[11] < 0.31177828:
                    if input[10] < 0.37548056:
                        var45 = 0.043506283
                    else:
                        var45 = 0.018806549
                else:
                    if input[2] < 99.0:
                        var45 = 0.035741672
                    else:
                        var45 = -0.0111098485
    var46 = var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44 + var45
    if input[7] < 139.0:
        if input[7] < 64.0:
            if input[7] < 38.0:
                if input[19] < 43.5507:
                    if input[12] < 0.1300813:
                        var47 = -0.0042351666
                    else:
                        var47 = 0.019206325
                else:
                    if input[12] < 0.10803619:
                        var47 = 0.01763981
                    else:
                        var47 = 0.023495397
            else:
                if input[30] < 11.0:
                    if input[12] < 0.19067797:
                        var47 = 0.02120785
                    else:
                        var47 = 0.026626343
                else:
                    if input[11] < 0.25187203:
                        var47 = 0.02736781
                    else:
                        var47 = 0.022886025
        else:
            if input[30] < 11.0:
                if input[10] < 0.3962926:
                    if input[11] < 0.28282827:
                        var47 = 0.027576445
                    else:
                        var47 = 0.021109212
                else:
                    if input[12] < 0.10382322:
                        var47 = -0.039877217
                    else:
                        var47 = 0.008751364
            else:
                if input[13] < 0.43035862:
                    if input[11] < 0.2893082:
                        var47 = 0.031225184
                    else:
                        var47 = 0.026527513
                else:
                    if input[11] < 0.260095:
                        var47 = 0.025822539
                    else:
                        var47 = 0.010444673
    else:
        if input[7] < 319.0:
            if input[30] < 13.0:
                if input[12] < 0.13622755:
                    if input[11] < 0.088716626:
                        var47 = -0.030987997
                    else:
                        var47 = 0.027292505
                else:
                    if input[10] < 0.13217391:
                        var47 = 0.026472444
                    else:
                        var47 = 0.032625098
            else:
                if input[11] < 0.2656396:
                    if input[30] < 18.0:
                        var47 = 0.03442356
                    else:
                        var47 = 0.036842093
                else:
                    if input[11] < 0.34256172:
                        var47 = 0.032077488
                    else:
                        var47 = 0.023632485
        else:
            if input[30] < 17.0:
                if input[12] < 0.21595487:
                    if input[30] < 11.0:
                        var47 = 0.031499106
                    else:
                        var47 = 0.035424452
                else:
                    if input[22] < 5.2245884:
                        var47 = 0.035508938
                    else:
                        var47 = 0.038640644
            else:
                if input[7] < 839.0:
                    if input[11] < 0.22622779:
                        var47 = 0.039237365
                    else:
                        var47 = 0.036375962
                else:
                    if input[15] < 31.0:
                        var47 = 0.011957078
                    else:
                        var47 = 0.041578565
    if input[7] < 222.0:
        if input[7] < 106.0:
            if input[7] < 58.0:
                if input[22] < 4.7004967:
                    if input[12] < 0.13118812:
                        var48 = 0.0149402935
                    else:
                        var48 = 0.021945354
                else:
                    if input[13] < 0.41038525:
                        var48 = 0.025288431
                    else:
                        var48 = 0.01935474
            else:
                if input[30] < 16.0:
                    if input[10] < 0.35:
                        var48 = 0.025616977
                    else:
                        var48 = 0.016128117
                else:
                    if input[6] < 209.0:
                        var48 = 0.029439664
                    else:
                        var48 = 0.02287159
        else:
            if input[30] < 11.0:
                if input[12] < 0.16605166:
                    if input[11] < 0.124938026:
                        var48 = 0.008479097
                    else:
                        var48 = 0.02484732
                else:
                    if input[10] < 0.17046413:
                        var48 = 0.02447592
                    else:
                        var48 = 0.029264435
            else:
                if input[12] < 0.20930232:
                    if input[12] < 0.09598741:
                        var48 = 0.024092639
                    else:
                        var48 = 0.030006615
                else:
                    if input[11] < 0.28440368:
                        var48 = 0.03237738
                    else:
                        var48 = 0.02226717
    else:
        if input[7] < 819.0:
            if input[30] < 13.0:
                if input[11] < 0.28:
                    if input[10] < 0.2425871:
                        var48 = 0.032763995
                    else:
                        var48 = 0.029978504
                else:
                    if input[11] < 0.38214287:
                        var48 = 0.02740317
                    else:
                        var48 = 0.008258534
            else:
                if input[11] < 0.24146982:
                    if input[10] < 0.31132075:
                        var48 = 0.035411805
                    else:
                        var48 = 0.030273974
                else:
                    if input[11] < 0.3506606:
                        var48 = 0.032624297
                    else:
                        var48 = 0.024324179
        else:
            if input[11] < 0.25804585:
                if input[10] < 0.33200124:
                    if input[30] < 17.0:
                        var48 = 0.036737565
                    else:
                        var48 = 0.03962249
                else:
                    if input[25] < 0.0033013327:
                        var48 = 0.030642569
                    else:
                        var48 = 0.012074429
            else:
                if input[22] < 4.937772:
                    if input[12] < 0.21722114:
                        var48 = 0.028527467
                    else:
                        var48 = 0.0039897435
                else:
                    if input[13] < 0.42651758:
                        var48 = 0.03451694
                    else:
                        var48 = 0.020729385
    if input[7] < 189.0:
        if input[7] < 84.0:
            if input[7] < 44.0:
                if input[30] < 10.0:
                    if input[12] < 0.10969388:
                        var49 = 0.0018656284
                    else:
                        var49 = 0.015896408
                else:
                    if input[11] < 0.25443786:
                        var49 = 0.020681474
                    else:
                        var49 = 0.016235735
            else:
                if input[30] < 18.0:
                    if input[11] < 0.27471566:
                        var49 = 0.02297591
                    else:
                        var49 = 0.018691506
                else:
                    if input[12] < 0.113520406:
                        var49 = 0.021928225
                    else:
                        var49 = 0.028990148
        else:
            if input[30] < 16.0:
                if input[11] < 0.3178114:
                    if input[35] < 17.271885:
                        var49 = 0.019385165
                    else:
                        var49 = 0.026492584
                else:
                    if input[13] < 0.41821945:
                        var49 = 0.019060818
                    else:
                        var49 = -0.012226432
            else:
                if input[11] < 0.25187203:
                    if input[35] < 17.88721:
                        var49 = 0.02746062
                    else:
                        var49 = 0.030678341
                else:
                    if input[11] < 0.3506606:
                        var49 = 0.02700623
                    else:
                        var49 = 0.017071297
    else:
        if input[7] < 427.0:
            if input[11] < 0.2785235:
                if input[30] < 11.0:
                    if input[13] < 0.45728898:
                        var49 = 0.028036265
                    else:
                        var49 = 0.0070668655
                else:
                    if input[12] < 0.17378917:
                        var49 = 0.029412556
                    else:
                        var49 = 0.03170332
            else:
                if input[30] < 11.0:
                    if input[7] < 413.0:
                        var49 = 0.019803127
                    else:
                        var49 = -0.032303285
                else:
                    if input[10] < 0.10353011:
                        var49 = 0.01854184
                    else:
                        var49 = 0.027827496
        else:
            if input[22] < 5.385421:
                if input[11] < 0.3019608:
                    if input[10] < 0.33581847:
                        var49 = 0.031166373
                    else:
                        var49 = 0.016177831
                else:
                    if input[4] < 10028.0:
                        var49 = 0.024160026
                    else:
                        var49 = 0.010567374
            else:
                if input[12] < 0.13231552:
                    if input[1] < 1.6584686:
                        var49 = -0.0013437471
                    else:
                        var49 = 0.028652197
                else:
                    if input[11] < 0.25804585:
                        var49 = 0.034859844
                    else:
                        var49 = 0.031501576
    if input[7] < 245.0:
        if input[7] < 106.0:
            if input[7] < 63.0:
                if input[30] < 12.0:
                    if input[12] < 0.14443277:
                        var50 = 0.013793572
                    else:
                        var50 = 0.019107535
                else:
                    if input[10] < 0.18523775:
                        var50 = 0.011723792
                    else:
                        var50 = 0.021287784
            else:
                if input[11] < 0.29545453:
                    if input[13] < 0.4027778:
                        var50 = 0.02377978
                    else:
                        var50 = 0.020200389
                else:
                    if input[13] < 0.41821945:
                        var50 = 0.017937759
                    else:
                        var50 = -0.008303176
        else:
            if input[30] < 11.0:
                if input[0] < 3171.0:
                    if input[11] < 0.29322034:
                        var50 = 0.023652954
                    else:
                        var50 = 0.017414356
                else:
                    var50 = -0.031391665
            else:
                if input[30] < 18.0:
                    if input[11] < 0.24758454:
                        var50 = 0.026624372
                    else:
                        var50 = 0.024046563
                else:
                    if input[12] < 0.16605166:
                        var50 = 0.026607037
                    else:
                        var50 = 0.029927382
    else:
        if input[30] < 17.0:
            if input[12] < 0.19128329:
                if input[12] < 0.12776025:
                    if input[16] < 38.773506:
                        var50 = 0.022116946
                    else:
                        var50 = 0.031799477
                else:
                    if input[5] < 225.0:
                        var50 = 0.01623152
                    else:
                        var50 = 0.027816305
            else:
                if input[11] < 0.24857685:
                    if input[15] < 30.0:
                        var50 = 0.028942937
                    else:
                        var50 = 0.031550452
                else:
                    if input[22] < 5.137559:
                        var50 = 0.023340395
                    else:
                        var50 = 0.027948571
        else:
            if input[7] < 839.0:
                if input[11] < 0.31177828:
                    if input[12] < 0.20179372:
                        var50 = 0.030063212
                    else:
                        var50 = 0.032258015
                else:
                    if input[10] < 0.23703703:
                        var50 = 0.02537829
                    else:
                        var50 = 0.0011644283
            else:
                if input[15] < 31.0:
                    if input[10] < 0.2976695:
                        var50 = 0.014667273
                    else:
                        var50 = -0.023929186
                else:
                    if input[12] < 0.14285715:
                        var50 = 0.028298963
                    else:
                        var50 = 0.034922555
    if input[7] < 146.0:
        if input[7] < 73.0:
            if input[7] < 41.0:
                if input[22] < 3.9122171:
                    if input[6] < 87.0:
                        var51 = 0.012044926
                    else:
                        var51 = -0.007993848
                else:
                    if input[8] < 197.0:
                        var51 = 0.016261037
                    else:
                        var51 = 0.0017774443
            else:
                if input[6] < 99.0:
                    if input[10] < 0.30397022:
                        var51 = 0.020174062
                    else:
                        var51 = 0.015360675
                else:
                    if input[10] < 0.18052904:
                        var51 = 0.0104623465
                    else:
                        var51 = 0.017561797
        else:
            if input[30] < 12.0:
                if input[11] < 0.2875817:
                    if input[35] < 17.728792:
                        var51 = 0.016092112
                    else:
                        var51 = 0.021412997
                else:
                    if input[10] < 0.10353011:
                        var51 = -0.0065107928
                    else:
                        var51 = 0.014966714
            else:
                if input[12] < 0.09598741:
                    if input[13] < 0.41955444:
                        var51 = 0.01883908
                    else:
                        var51 = 0.00841553
                else:
                    if input[30] < 17.0:
                        var51 = 0.022581726
                    else:
                        var51 = 0.024976926
    else:
        if input[7] < 358.0:
            if input[11] < 0.24074075:
                if input[30] < 11.0:
                    if input[10] < 0.305761:
                        var51 = 0.023863038
                    else:
                        var51 = 0.01561631
                else:
                    if input[30] < 18.0:
                        var51 = 0.02600548
                    else:
                        var51 = 0.02853865
            else:
                if input[11] < 0.34256172:
                    if input[20] < 16.160343:
                        var51 = 0.02205024
                    else:
                        var51 = 0.024981478
                else:
                    if input[10] < 0.14055482:
                        var51 = 0.010984426
                    else:
                        var51 = 0.021270024
        else:
            if input[30] < 13.0:
                if input[12] < 0.13622755:
                    if input[24] < 62505.0:
                        var51 = 0.012228694
                    else:
                        var51 = 0.022287732
                else:
                    if input[11] < 0.32142857:
                        var51 = 0.026889745
                    else:
                        var51 = 0.01758569
            else:
                if input[12] < 0.20644216:
                    if input[22] < 6.441144:
                        var51 = 0.026439566
                    else:
                        var51 = 0.029190416
                else:
                    if input[7] < 1163.0:
                        var51 = 0.02984122
                    else:
                        var51 = 0.03278141
    if input[7] < 128.0:
        if input[30] < 11.0:
            if input[12] < 0.13118812:
                if input[19] < 47.51207:
                    if input[13] < 0.3423729:
                        var52 = -0.01853592
                    else:
                        var52 = -0.0017794324
                else:
                    if input[10] < 0.35634327:
                        var52 = 0.012853103
                    else:
                        var52 = -0.0030176796
            else:
                if input[11] < 0.3506606:
                    if input[13] < 0.4054945:
                        var52 = 0.01788345
                    else:
                        var52 = 0.013290192
                else:
                    if input[5] < 80.0:
                        var52 = -0.01620875
                    else:
                        var52 = 0.010134994
        else:
            if input[12] < 0.17320575:
                if input[29] < 41.0:
                    if input[13] < 0.34507042:
                        var52 = -0.014279804
                    else:
                        var52 = 0.005819427
                else:
                    if input[12] < 0.10803619:
                        var52 = 0.015279414
                    else:
                        var52 = 0.019268941
            else:
                if input[10] < 0.13652053:
                    if input[30] < 14.0:
                        var52 = 0.007129207
                    else:
                        var52 = 0.020004742
                else:
                    if input[11] < 0.26459855:
                        var52 = 0.021913897
                    else:
                        var52 = 0.016933307
    else:
        if input[7] < 319.0:
            if input[30] < 16.0:
                if input[11] < 0.24074075:
                    if input[10] < 0.2683706:
                        var52 = 0.023578906
                    else:
                        var52 = 0.020361846
                else:
                    if input[33] < 41827.0:
                        var52 = 0.020246318
                    else:
                        var52 = 0.012452296
            else:
                if input[12] < 0.1473772:
                    if input[10] < 0.13652053:
                        var52 = 0.002925767
                    else:
                        var52 = 0.022322252
                else:
                    if input[6] < 52.0:
                        var52 = 0.008063312
                    else:
                        var52 = 0.025312642
        else:
            if input[30] < 12.0:
                if input[12] < 0.15118197:
                    if input[10] < 0.13926017:
                        var52 = -0.00021361785
                    else:
                        var52 = 0.01928544
                else:
                    if input[11] < 0.3178114:
                        var52 = 0.02432031
                    else:
                        var52 = 0.014845152
            else:
                if input[12] < 0.20644216:
                    if input[22] < 6.441144:
                        var52 = 0.024250934
                    else:
                        var52 = 0.027074367
                else:
                    if input[15] < 35.0:
                        var52 = 0.02689748
                    else:
                        var52 = 0.02939766
    if input[7] < 222.0:
        if input[7] < 89.0:
            if input[30] < 14.0:
                if input[12] < 0.13718492:
                    if input[33] < 3948.0:
                        var53 = -0.005120458
                    else:
                        var53 = 0.0122408895
                else:
                    if input[13] < 0.4054945:
                        var53 = 0.016368708
                    else:
                        var53 = 0.012579006
            else:
                if input[8] < 615.0:
                    if input[11] < 0.25270757:
                        var53 = 0.019124389
                    else:
                        var53 = 0.015648454
                else:
                    if input[5] < 442.0:
                        var53 = -0.021626411
                    else:
                        var53 = 0.00728731
        else:
            if input[30] < 16.0:
                if input[12] < 0.14356436:
                    if input[11] < 0.113788486:
                        var53 = -0.003969894
                    else:
                        var53 = 0.016368184
                else:
                    if input[10] < 0.1519871:
                        var53 = 0.015972724
                    else:
                        var53 = 0.020148955
            else:
                if input[12] < 0.168435:
                    if input[10] < 0.14757554:
                        var53 = 0.009377236
                    else:
                        var53 = 0.020369938
                else:
                    if input[11] < 0.08375:
                        var53 = 0.009990714
                    else:
                        var53 = 0.022757271
    else:
        if input[15] < 36.0:
            if input[11] < 0.23636363:
                if input[10] < 0.31335953:
                    if input[15] < 28.0:
                        var53 = 0.021897623
                    else:
                        var53 = 0.024624957
                else:
                    if input[24] < 28989.0:
                        var53 = 0.010495802
                    else:
                        var53 = 0.018618584
            else:
                if input[30] < 11.0:
                    if input[11] < 0.29322034:
                        var53 = 0.019342382
                    else:
                        var53 = 0.012986058
                else:
                    if input[10] < 0.15306123:
                        var53 = 0.019426852
                    else:
                        var53 = 0.022444976
        else:
            if input[12] < 0.17320575:
                if input[10] < 0.110275686:
                    if input[4] < 10162.0:
                        var53 = 0.012240372
                    else:
                        var53 = -0.022565007
                else:
                    if input[12] < 0.080063626:
                        var53 = 0.013581865
                    else:
                        var53 = 0.023941966
            else:
                if input[11] < 0.22882883:
                    if input[12] < 0.2877698:
                        var53 = 0.027243553
                    else:
                        var53 = 0.03064093
                else:
                    if input[11] < 0.31177828:
                        var53 = 0.025376692
                    else:
                        var53 = 0.01807635
    if input[7] < 245.0:
        if input[7] < 115.0:
            if input[7] < 63.0:
                if input[30] < 16.0:
                    if input[12] < 0.13231552:
                        var54 = 0.009805613
                    else:
                        var54 = 0.013448797
                else:
                    if input[16] < 28.528854:
                        var54 = 0.017632842
                    else:
                        var54 = 0.0022531503
            else:
                if input[30] < 10.0:
                    if input[8] < 310.0:
                        var54 = 0.013801433
                    else:
                        var54 = -0.0003664226
                else:
                    if input[13] < 0.42833108:
                        var54 = 0.017077109
                    else:
                        var54 = 0.011386573
        else:
            if input[30] < 11.0:
                if input[10] < 0.30397022:
                    if input[10] < 0.16962588:
                        var54 = 0.013278264
                    else:
                        var54 = 0.017932734
                else:
                    if input[1] < 3.973512:
                        var54 = -0.0014408987
                    else:
                        var54 = 0.012395262
            else:
                if input[12] < 0.22857143:
                    if input[13] < 0.39587975:
                        var54 = 0.019672997
                    else:
                        var54 = 0.017389467
                else:
                    if input[11] < 0.21859904:
                        var54 = 0.021984814
                    else:
                        var54 = 0.017575713
    else:
        if input[30] < 17.0:
            if input[12] < 0.19128329:
                if input[12] < 0.12541376:
                    if input[13] < 0.44163424:
                        var54 = 0.016588118
                    else:
                        var54 = 0.00477765
                else:
                    if input[30] < 10.0:
                        var54 = 0.014849113
                    else:
                        var54 = 0.02042575
            else:
                if input[11] < 0.24595469:
                    if input[15] < 30.0:
                        var54 = 0.021220729
                    else:
                        var54 = 0.023496164
                else:
                    if input[10] < 0.07663783:
                        var54 = 0.009898508
                    else:
                        var54 = 0.019511927
        else:
            if input[12] < 0.2600229:
                if input[11] < 0.31177828:
                    if input[12] < 0.119382024:
                        var54 = 0.017907647
                    else:
                        var54 = 0.023622973
                else:
                    if input[10] < 0.23703703:
                        var54 = 0.017732691
                    else:
                        var54 = -0.005532477
            else:
                if input[29] < 1115.0:
                    if input[10] < 0.21693675:
                        var54 = 0.02620628
                    else:
                        var54 = 0.022823222
                else:
                    if input[3] < 6946.773:
                        var54 = 0.031990632
                    else:
                        var54 = 0.0064873877
    if input[7] < 164.0:
        if input[7] < 78.0:
            if input[30] < 16.0:
                if input[12] < 0.12776025:
                    if input[19] < 47.51207:
                        var55 = -0.008527881
                    else:
                        var55 = 0.010062632
                else:
                    if input[11] < 0.260095:
                        var55 = 0.013401777
                    else:
                        var55 = 0.009524031
            else:
                if input[12] < 0.11165048:
                    if input[22] < 5.532301:
                        var55 = 0.019829504
                    else:
                        var55 = 0.007683933
                else:
                    if input[16] < 20.977226:
                        var55 = 0.003433728
                    else:
                        var55 = 0.017692426
        else:
            if input[10] < 0.1463964:
                if input[12] < 0.23616236:
                    if input[5] < 71.0:
                        var55 = 0.0031681173
                    else:
                        var55 = 0.011614031
                else:
                    if input[20] < 11.595078:
                        var55 = 0.007892759
                    else:
                        var55 = 0.018028807
            else:
                if input[10] < 0.3643846:
                    if input[13] < 0.42833108:
                        var55 = 0.016746605
                    else:
                        var55 = 0.012422901
                else:
                    if input[2] < 58.0:
                        var55 = 0.011785901
                    else:
                        var55 = -0.003573639
    else:
        if input[7] < 409.0:
            if input[30] < 11.0:
                if input[13] < 0.45728898:
                    if input[11] < 0.2785235:
                        var55 = 0.016554622
                    else:
                        var55 = 0.010094657
                else:
                    if input[16] < 24.180304:
                        var55 = -0.024302742
                    else:
                        var55 = 0.0078121214
            else:
                if input[11] < 0.24074075:
                    if input[12] < 0.20179372:
                        var55 = 0.018548962
                    else:
                        var55 = 0.020578062
                else:
                    if input[10] < 0.110275686:
                        var55 = 0.010828067
                    else:
                        var55 = 0.017534262
        else:
            if input[22] < 5.5213284:
                if input[12] < 0.12893553:
                    if input[6] < 920.0:
                        var55 = -0.016965738
                    else:
                        var55 = 0.013227125
                else:
                    if input[10] < 0.110275686:
                        var55 = 0.01262237
                    else:
                        var55 = 0.019939966
            else:
                if input[12] < 0.16402878:
                    if input[10] < 0.110275686:
                        var55 = 0.00024142934
                    else:
                        var55 = 0.019619077
                else:
                    if input[11] < 0.22691293:
                        var55 = 0.023079528
                    else:
                        var55 = 0.020547235
    if input[7] < 245.0:
        if input[7] < 116.0:
            if input[30] < 10.0:
                if input[7] < 115.0:
                    if input[8] < 310.0:
                        var56 = 0.010134193
                    else:
                        var56 = -0.0017440965
                else:
                    if input[10] < 0.17830883:
                        var56 = -0.00049174554
                    else:
                        var56 = -0.06555852
            else:
                if input[12] < 0.1418919:
                    if input[5] < 61.0:
                        var56 = -0.000583132
                    else:
                        var56 = 0.011853422
                else:
                    if input[30] < 16.0:
                        var56 = 0.013483331
                    else:
                        var56 = 0.016495448
        else:
            if input[30] < 15.0:
                if input[12] < 0.15625:
                    if input[11] < 0.107586205:
                        var56 = -0.0059892773
                    else:
                        var56 = 0.012860457
                else:
                    if input[10] < 0.110275686:
                        var56 = 0.006770514
                    else:
                        var56 = 0.015743189
            else:
                if input[13] < 0.2934363:
                    if input[10] < 0.17680827:
                        var56 = 0.0261896
                    else:
                        var56 = 0.007899395
                else:
                    if input[13] < 0.42390525:
                        var56 = 0.017696397
                    else:
                        var56 = 0.013987171
    else:
        if input[30] < 18.0:
            if input[12] < 0.22336842:
                if input[10] < 0.3643846:
                    if input[30] < 10.0:
                        var56 = 0.012593269
                    else:
                        var56 = 0.017511124
                else:
                    if input[26] < 56.18348:
                        var56 = 0.0072447606
                    else:
                        var56 = -0.03083621
            else:
                if input[10] < 0.26643598:
                    if input[11] < 0.22691293:
                        var56 = 0.020367974
                    else:
                        var56 = 0.01697188
                else:
                    if input[13] < 0.39709917:
                        var56 = 0.014199316
                    else:
                        var56 = -0.0038804275
        else:
            if input[11] < 0.26459855:
                if input[7] < 493.0:
                    if input[0] < 3116.0:
                        var56 = 0.020243166
                    else:
                        var56 = 0.011770754
                else:
                    if input[12] < 0.24329026:
                        var56 = 0.021557327
                    else:
                        var56 = 0.024140337
            else:
                if input[7] < 1047.0:
                    if input[11] < 0.36167213:
                        var56 = 0.016862746
                    else:
                        var56 = 0.004557377
                else:
                    if input[26] < 2.9937801:
                        var56 = 0.0050844587
                    else:
                        var56 = 0.024357006
    if input[7] < 128.0:
        if input[30] < 10.0:
            if input[8] < 310.0:
                if input[11] < 0.36167213:
                    if input[2] < 94.0:
                        var57 = 0.008666621
                    else:
                        var57 = 0.016369283
                else:
                    if input[7] < 64.0:
                        var57 = -0.040230837
                    else:
                        var57 = 0.008240265
            else:
                if input[11] < 0.19019139:
                    if input[7] < 72.0:
                        var57 = 0.027453626
                    else:
                        var57 = -0.022800012
                else:
                    if input[8] < 330.0:
                        var57 = -0.018711606
                    else:
                        var57 = 0.006429599
        else:
            if input[12] < 0.1871969:
                if input[29] < 41.0:
                    if input[3] < 5001.6816:
                        var57 = 0.0041219373
                    else:
                        var57 = -0.010487179
                else:
                    if input[29] < 316.0:
                        var57 = 0.011987096
                    else:
                        var57 = 0.004520602
            else:
                if input[10] < 0.13926017:
                    if input[35] < 18.84348:
                        var57 = 0.0043323967
                    else:
                        var57 = 0.016143879
                else:
                    if input[30] < 13.0:
                        var57 = 0.0131506985
                    else:
                        var57 = 0.015476092
    else:
        if input[15] < 30.0:
            if input[12] < 0.20179372:
                if input[35] < 17.238165:
                    if input[4] < 11465.0:
                        var57 = 0.0070274593
                    else:
                        var57 = -0.02015123
                else:
                    if input[10] < 0.15306123:
                        var57 = 0.008477144
                    else:
                        var57 = 0.013912357
            else:
                if input[10] < 0.1486048:
                    if input[12] < 0.27208757:
                        var57 = 0.010765244
                    else:
                        var57 = 0.01487483
                else:
                    if input[10] < 0.24460432:
                        var57 = 0.017192071
                    else:
                        var57 = 0.0137369605
        else:
            if input[12] < 0.16605166:
                if input[10] < 0.14970563:
                    if input[12] < 0.08512975:
                        var57 = -0.021995803
                    else:
                        var57 = 0.01000235
                else:
                    if input[10] < 0.35:
                        var57 = 0.016004711
                    else:
                        var57 = 0.009344149
            else:
                if input[7] < 990.0:
                    if input[10] < 0.33200124:
                        var57 = 0.01768875
                    else:
                        var57 = 0.010723299
                else:
                    if input[10] < 0.07663783:
                        var57 = 0.009022137
                    else:
                        var57 = 0.020563604
    if input[7] < 266.0:
        if input[7] < 104.0:
            if input[30] < 18.0:
                if input[11] < 0.26183686:
                    if input[10] < 0.31768888:
                        var58 = 0.011047565
                    else:
                        var58 = 0.006807799
                else:
                    if input[13] < 0.41384995:
                        var58 = 0.0077762986
                    else:
                        var58 = -0.0010486348
            else:
                if input[2] < 93.0:
                    if input[11] < 0.0931677:
                        var58 = -0.0054736338
                    else:
                        var58 = 0.015209344
                else:
                    if input[35] < 17.957962:
                        var58 = -0.011083856
                    else:
                        var58 = 0.011914506
        else:
            if input[30] < 18.0:
                if input[35] < 17.271885:
                    if input[10] < 0.28091604:
                        var58 = 0.010128179
                    else:
                        var58 = -0.0061189677
                else:
                    if input[11] < 0.24220484:
                        var58 = 0.013577856
                    else:
                        var58 = 0.01123772
            else:
                if input[8] < 663.0:
                    if input[35] < 18.95267:
                        var58 = 0.016431594
                    else:
                        var58 = 0.012512398
                else:
                    if input[6] < 379.0:
                        var58 = 0.000836173
                    else:
                        var58 = 0.011571525
    else:
        if input[30] < 11.0:
            if input[12] < 0.13622755:
                if input[22] < 6.2262416:
                    if input[11] < 0.15488656:
                        var58 = -0.02370096
                    else:
                        var58 = 0.004408499
                else:
                    if input[6] < 2197.0:
                        var58 = 0.029946698
                    else:
                        var58 = -0.007663087
            else:
                if input[11] < 0.30646765:
                    if input[35] < 17.84448:
                        var58 = 0.010214443
                    else:
                        var58 = 0.014498303
                else:
                    if input[8] < 438.0:
                        var58 = -0.029549053
                    else:
                        var58 = 0.0072238706
        else:
            if input[7] < 703.0:
                if input[12] < 0.124279834:
                    if input[19] < 405.7972:
                        var58 = 0.011638749
                    else:
                        var58 = -0.018615358
                else:
                    if input[10] < 0.15306123:
                        var58 = 0.013853523
                    else:
                        var58 = 0.016324174
            else:
                if input[11] < 0.30880615:
                    if input[10] < 0.31768888:
                        var58 = 0.018434083
                    else:
                        var58 = 0.011566197
                else:
                    if input[16] < 34.75925:
                        var58 = -0.0039828173
                    else:
                        var58 = 0.013254272
    if input[7] < 245.0:
        if input[30] < 13.0:
            if input[12] < 0.13622755:
                if input[19] < 50.294167:
                    if input[13] < 0.3423729:
                        var59 = -0.020660609
                    else:
                        var59 = -0.0026862652
                else:
                    if input[11] < 0.088716626:
                        var59 = -0.03540901
                    else:
                        var59 = 0.007081496
            else:
                if input[7] < 119.0:
                    if input[35] < 17.728792:
                        var59 = 0.005387363
                    else:
                        var59 = 0.009572381
                else:
                    if input[10] < 0.13217391:
                        var59 = 0.005700987
                    else:
                        var59 = 0.011769808
        else:
            if input[12] < 0.171415:
                if input[15] < 28.0:
                    if input[10] < 0.16133004:
                        var59 = 0.00073397387
                    else:
                        var59 = 0.009551708
                else:
                    if input[12] < 0.09598741:
                        var59 = 0.007742207
                    else:
                        var59 = 0.012562816
            else:
                if input[11] < 0.2256:
                    if input[10] < 0.35:
                        var59 = 0.013918805
                    else:
                        var59 = 0.00012015095
                else:
                    if input[19] < 160.84395:
                        var59 = 0.011201387
                    else:
                        var59 = 0.022669647
    else:
        if input[15] < 37.0:
            if input[11] < 0.23636363:
                if input[10] < 0.29475984:
                    if input[13] < 0.41821945:
                        var59 = 0.015503304
                    else:
                        var59 = 0.012281265
                else:
                    if input[10] < 0.3394348:
                        var59 = 0.0119736
                    else:
                        var59 = 0.0062660086
            else:
                if input[11] < 0.30880615:
                    if input[35] < 17.908493:
                        var59 = 0.0076485686
                    else:
                        var59 = 0.012826348
                else:
                    if input[10] < 0.110275686:
                        var59 = 0.0028601713
                    else:
                        var59 = 0.010299814
        else:
            if input[12] < 0.2877698:
                if input[12] < 0.12069428:
                    if input[35] < 17.238165:
                        var59 = -0.00033671357
                    else:
                        var59 = 0.012546616
                else:
                    if input[29] < 221.0:
                        var59 = 0.0077095027
                    else:
                        var59 = 0.016542148
            else:
                if input[1] < 7.2376733:
                    if input[24] < 161555.0:
                        var59 = 0.02247397
                    else:
                        var59 = -0.0016616964
                else:
                    if input[10] < 0.09894699:
                        var59 = -0.0017630684
                    else:
                        var59 = 0.017405411
    if input[7] < 139.0:
        if input[30] < 11.0:
            if input[10] < 0.32578397:
                if input[12] < 0.19665273:
                    if input[5] < 82.0:
                        var60 = 0.0033112105
                    else:
                        var60 = 0.0076559368
                else:
                    if input[15] < 28.0:
                        var60 = 0.009673673
                    else:
                        var60 = -0.009327488
            else:
                if input[5] < 458.0:
                    if input[1] < 3.1898355:
                        var60 = -0.021503152
                    else:
                        var60 = 0.0026925376
                else:
                    if input[15] < 28.0:
                        var60 = 0.0020211863
                    else:
                        var60 = -0.04800799
        else:
            if input[13] < 0.42833108:
                if input[11] < 0.24074075:
                    if input[10] < 0.2831126:
                        var60 = 0.011656835
                    else:
                        var60 = 0.008622553
                else:
                    if input[5] < 100.0:
                        var60 = 0.0061007724
                    else:
                        var60 = 0.009669849
            else:
                if input[10] < 0.15960912:
                    if input[12] < 0.15749696:
                        var60 = -0.015148546
                    else:
                        var60 = 0.00467045
                else:
                    if input[10] < 0.26:
                        var60 = 0.00830764
                    else:
                        var60 = -0.0017757891
    else:
        if input[30] < 17.0:
            if input[12] < 0.22401847:
                if input[11] < 0.123484015:
                    if input[12] < 0.11165048:
                        var60 = -0.0136753395
                    else:
                        var60 = 0.006942673
                else:
                    if input[5] < 124.0:
                        var60 = 0.003453362
                    else:
                        var60 = 0.011357727
            else:
                if input[10] < 0.26643598:
                    if input[19] < 176.25294:
                        var60 = 0.0125962645
                    else:
                        var60 = 0.015252091
                else:
                    if input[7] < 143.0:
                        var60 = -0.019628882
                    else:
                        var60 = 0.007868916
        else:
            if input[12] < 0.2692793:
                if input[7] < 765.0:
                    if input[13] < 0.4041451:
                        var60 = 0.013834319
                    else:
                        var60 = 0.011299365
                else:
                    if input[10] < 0.37548056:
                        var60 = 0.016018549
                    else:
                        var60 = -0.016695017
            else:
                if input[5] < 65.0:
                    var60 = -0.034823313
                else:
                    if input[25] < 0.0009489633:
                        var60 = 0.022363411
                    else:
                        var60 = 0.016498407
    if input[7] < 266.0:
        if input[7] < 78.0:
            if input[12] < 0.09328358:
                if input[1] < 7.6474423:
                    if input[1] < 7.476715:
                        var61 = 0.00047322005
                    else:
                        var61 = -0.029817117
                else:
                    if input[20] < 11.754217:
                        var61 = -0.007654947
                    else:
                        var61 = 0.0115704825
            else:
                if input[30] < 18.0:
                    if input[4] < 10923.0:
                        var61 = 0.0065373885
                    else:
                        var61 = 0.010519108
                else:
                    if input[2] < 93.0:
                        var61 = 0.012690827
                    else:
                        var61 = 0.0017526094
        else:
            if input[11] < 0.3178114:
                if input[30] < 15.0:
                    if input[10] < 0.31335953:
                        var61 = 0.009497269
                    else:
                        var61 = 0.005116459
                else:
                    if input[13] < 0.42390525:
                        var61 = 0.011367655
                    else:
                        var61 = 0.007426093
            else:
                if input[22] < 5.1475143:
                    if input[35] < 18.189157:
                        var61 = -0.021913601
                    else:
                        var61 = 0.0023115382
                else:
                    if input[25] < 0.13048932:
                        var61 = 0.008168324
                    else:
                        var61 = -0.00079830684
    else:
        if input[30] < 12.0:
            if input[30] < 10.0:
                if input[35] < 17.531393:
                    if input[22] < 5.5116053:
                        var61 = -0.006891403
                    else:
                        var61 = 0.012956816
                else:
                    if input[11] < 0.3019608:
                        var61 = 0.009394924
                    else:
                        var61 = -0.0000073084775
            else:
                if input[13] < 0.33932462:
                    if input[6] < 2527.0:
                        var61 = 0.008666394
                    else:
                        var61 = -0.013764086
                else:
                    if input[12] < 0.2320377:
                        var61 = 0.010237526
                    else:
                        var61 = 0.01330975
        else:
            if input[12] < 0.12069428:
                if input[11] < 0.115555555:
                    if input[11] < 0.07709251:
                        var61 = 0.007162083
                    else:
                        var61 = -0.024323199
                else:
                    if input[1] < 8.927292:
                        var61 = 0.009307324
                    else:
                        var61 = 0.0011662644
            else:
                if input[15] < 36.0:
                    if input[13] < 0.41821945:
                        var61 = 0.0126228435
                    else:
                        var61 = 0.0097052315
                else:
                    if input[11] < 0.31177828:
                        var61 = 0.0143628195
                    else:
                        var61 = 0.008351473
    if input[7] < 128.0:
        if input[30] < 10.0:
            if input[8] < 310.0:
                if input[2] < 94.0:
                    if input[11] < 0.36167213:
                        var62 = 0.0046599745
                    else:
                        var62 = -0.02395323
                else:
                    if input[5] < 71.0:
                        var62 = -0.0018356545
                    else:
                        var62 = 0.016854675
            else:
                if input[1] < 5.8652153:
                    if input[1] < 4.5170293:
                        var62 = -0.013023153
                    else:
                        var62 = 0.011843539
                else:
                    if input[11] < 0.3019608:
                        var62 = -0.006841492
                    else:
                        var62 = -0.03877194
        else:
            if input[8] < 581.0:
                if input[7] < 63.0:
                    if input[12] < 0.2320377:
                        var62 = 0.0057247053
                    else:
                        var62 = 0.012878909
                else:
                    if input[13] < 0.43035862:
                        var62 = 0.008598966
                    else:
                        var62 = 0.0039450224
            else:
                if input[5] < 286.0:
                    if input[1] < 4.485425:
                        var62 = -0.012815154
                    else:
                        var62 = -0.052070923
                else:
                    if input[20] < 17.908752:
                        var62 = -0.008880707
                    else:
                        var62 = 0.009365114
    else:
        if input[30] < 18.0:
            if input[12] < 0.22401847:
                if input[15] < 28.0:
                    if input[13] < 0.45338568:
                        var62 = 0.007887698
                    else:
                        var62 = -0.0025404578
                else:
                    if input[10] < 0.31991714:
                        var62 = 0.010000386
                    else:
                        var62 = 0.005647559
            else:
                if input[10] < 0.26643598:
                    if input[11] < 0.22691293:
                        var62 = 0.011955876
                    else:
                        var62 = 0.008777889
                else:
                    if input[15] < 22.0:
                        var62 = -0.011139469
                    else:
                        var62 = 0.006457222
        else:
            if input[11] < 0.21907601:
                if input[35] < 17.718607:
                    if input[6] < 52.0:
                        var62 = -0.03526097
                    else:
                        var62 = 0.010905729
                else:
                    if input[7] < 500.0:
                        var62 = 0.012852934
                    else:
                        var62 = 0.015404916
            else:
                if input[13] < 0.39241052:
                    if input[10] < 0.29319373:
                        var62 = 0.011794106
                    else:
                        var62 = 0.004490593
                else:
                    if input[22] < 7.023741:
                        var62 = 0.0068959123
                    else:
                        var62 = 0.011883782
    if input[15] < 30.0:
        if input[12] < 0.16666667:
            if input[5] < 55.0:
                if input[16] < 23.413408:
                    if input[13] < 0.34507042:
                        var63 = -0.013311932
                    else:
                        var63 = -0.00027222442
                else:
                    var63 = -0.03258771
            else:
                if input[13] < 0.41095892:
                    if input[10] < 0.31335953:
                        var63 = 0.00703093
                    else:
                        var63 = 0.0040841727
                else:
                    if input[29] < 645.0:
                        var63 = 0.004034279
                    else:
                        var63 = -0.011122133
        else:
            if input[30] < 12.0:
                if input[10] < 0.1270073:
                    if input[16] < 30.821146:
                        var63 = 0.0031977803
                    else:
                        var63 = -0.023054907
                else:
                    if input[11] < 0.0931677:
                        var63 = -0.0007520395
                    else:
                        var63 = 0.007673606
            else:
                if input[10] < 0.14970563:
                    if input[12] < 0.24329026:
                        var63 = 0.0042318157
                    else:
                        var63 = 0.008260327
                else:
                    if input[10] < 0.26643598:
                        var63 = 0.009960956
                    else:
                        var63 = 0.007089101
    else:
        if input[12] < 0.1300813:
            if input[11] < 0.12880678:
                if input[22] < 5.5116053:
                    if input[8] < 555.0:
                        var63 = 0.0040673576
                    else:
                        var63 = -0.0400664
                else:
                    if input[4] < 7652.0:
                        var63 = 0.0018766964
                    else:
                        var63 = -0.019546226
            else:
                if input[10] < 0.14757554:
                    if input[16] < 34.891605:
                        var63 = -0.009308777
                    else:
                        var63 = 0.011764135
                else:
                    if input[13] < 0.39669928:
                        var63 = 0.009180877
                    else:
                        var63 = 0.005421233
        else:
            if input[12] < 0.28242075:
                if input[10] < 0.10747664:
                    if input[11] < 0.36167213:
                        var63 = 0.006161347
                    else:
                        var63 = -0.0069325804
                else:
                    if input[15] < 36.0:
                        var63 = 0.00977222
                    else:
                        var63 = 0.011640572
            else:
                if input[22] < 4.8675985:
                    if input[11] < 0.1954638:
                        var63 = 0.026897052
                    else:
                        var63 = -0.014216992
                else:
                    if input[25] < 0.00077370566:
                        var63 = 0.018027095
                    else:
                        var63 = 0.012266779
    if input[7] < 266.0:
        if input[30] < 13.0:
            if input[12] < 0.19414414:
                if input[19] < 67.94796:
                    if input[12] < 0.10144927:
                        var64 = -0.0056176004
                    else:
                        var64 = 0.0030659323
                else:
                    if input[10] < 0.19875777:
                        var64 = 0.0030826072
                    else:
                        var64 = 0.0060741
            else:
                if input[10] < 0.13217391:
                    if input[4] < 13595.0:
                        var64 = 0.0026464933
                    else:
                        var64 = -0.03258748
                else:
                    if input[11] < 0.0931677:
                        var64 = -0.0011107046
                    else:
                        var64 = 0.007647443
        else:
            if input[12] < 0.09598741:
                if input[10] < 0.14310052:
                    if input[3] < 5420.476:
                        var64 = -0.01819119
                    else:
                        var64 = 0.009440412
                else:
                    if input[30] < 15.0:
                        var64 = -0.0007539532
                    else:
                        var64 = 0.0052491627
            else:
                if input[35] < 19.480465:
                    if input[30] < 18.0:
                        var64 = 0.007576663
                    else:
                        var64 = 0.009502678
                else:
                    if input[10] < 0.2961165:
                        var64 = 0.003949707
                    else:
                        var64 = -0.0075826845
    else:
        if input[30] < 10.0:
            if input[11] < 0.07709251:
                if input[7] < 395.0:
                    var64 = -0.057200253
                else:
                    if input[16] < 26.685286:
                        var64 = 0.009853357
                    else:
                        var64 = -0.014635585
            else:
                if input[13] < 0.44163424:
                    if input[12] < 0.23616236:
                        var64 = 0.004328215
                    else:
                        var64 = 0.0088424245
                else:
                    if input[22] < 4.2844787:
                        var64 = -0.04542813
                    else:
                        var64 = 0.0004698217
        else:
            if input[11] < 0.25804585:
                if input[10] < 0.26071286:
                    if input[13] < 0.43141693:
                        var64 = 0.010596368
                    else:
                        var64 = 0.007381258
                else:
                    if input[15] < 33.0:
                        var64 = 0.005789595
                    else:
                        var64 = 0.009602121
            else:
                if input[10] < 0.110275686:
                    if input[11] < 0.32557118:
                        var64 = 0.0059158294
                    else:
                        var64 = -0.0015695688
                else:
                    if input[35] < 18.283422:
                        var64 = 0.004745318
                    else:
                        var64 = 0.008857845
    if input[7] < 128.0:
        if input[30] < 10.0:
            if input[8] < 310.0:
                if input[12] < 0.07342466:
                    if input[2] < 50.0:
                        var65 = -0.05817262
                    else:
                        var65 = 0.001849014
                else:
                    if input[2] < 94.0:
                        var65 = 0.0030670636
                    else:
                        var65 = 0.00985382
            else:
                if input[11] < 0.19019139:
                    if input[13] < 0.41753653:
                        var65 = -0.0063802633
                    else:
                        var65 = -0.0401793
                else:
                    if input[8] < 330.0:
                        var65 = -0.020825109
                    else:
                        var65 = 0.002136615
        else:
            if input[29] < 316.0:
                if input[11] < 0.25804585:
                    if input[35] < 17.571428:
                        var65 = 0.0036040004
                    else:
                        var65 = 0.0066371816
                else:
                    if input[13] < 0.41893157:
                        var65 = 0.004569082
                    else:
                        var65 = -0.0024519449
            else:
                if input[17] < 1494.0:
                    if input[30] < 15.0:
                        var65 = -0.04650442
                    else:
                        var65 = -0.006947922
                else:
                    if input[35] < 17.738255:
                        var65 = -0.009535424
                    else:
                        var65 = 0.0029821272
    else:
        if input[30] < 18.0:
            if input[12] < 0.22401847:
                if input[10] < 0.1558642:
                    if input[15] < 41.0:
                        var65 = 0.004023426
                    else:
                        var65 = 0.014734044
                else:
                    if input[10] < 0.33581847:
                        var65 = 0.007265217
                    else:
                        var65 = 0.0029404582
            else:
                if input[10] < 0.26643598:
                    if input[11] < 0.2211939:
                        var65 = 0.009238169
                    else:
                        var65 = 0.0065688016
                else:
                    if input[13] < 0.39510748:
                        var65 = 0.0045673437
                    else:
                        var65 = -0.009004564
        else:
            if input[11] < 0.20704846:
                if input[10] < 0.29043126:
                    if input[5] < 423.0:
                        var65 = 0.009971885
                    else:
                        var65 = 0.012207887
                else:
                    if input[6] < 52.0:
                        var65 = -0.043801453
                    else:
                        var65 = 0.00792171
            else:
                if input[15] < 45.0:
                    if input[13] < 0.39241052:
                        var65 = 0.00882532
                    else:
                        var65 = 0.0059593692
                else:
                    if input[22] < 7.884595:
                        var65 = 0.008765018
                    else:
                        var65 = 0.020713214
    if input[15] < 28.0:
        if input[12] < 0.17261904:
            if input[29] < 41.0:
                if input[10] < 0.2820513:
                    if input[11] < 0.2281106:
                        var66 = 0.0050942334
                    else:
                        var66 = -0.0046351454
                else:
                    if input[11] < 0.163134:
                        var66 = -0.0018273434
                    else:
                        var66 = -0.02197775
            else:
                if input[13] < 0.41323647:
                    if input[30] < 16.0:
                        var66 = 0.004024213
                    else:
                        var66 = 0.007401877
                else:
                    if input[17] < 2466.0:
                        var66 = 0.0025714503
                    else:
                        var66 = -0.0065406202
        else:
            if input[11] < 0.2875817:
                if input[30] < 13.0:
                    if input[13] < 0.4027778:
                        var66 = 0.0059746993
                    else:
                        var66 = 0.0033485317
                else:
                    if input[5] < 660.0:
                        var66 = 0.0074538747
                    else:
                        var66 = -0.023742426
            else:
                if input[1] < 8.978:
                    if input[29] < 41.0:
                        var66 = 0.0123597225
                    else:
                        var66 = 0.00060855394
                else:
                    if input[12] < 0.19248678:
                        var66 = 0.0023568757
                    else:
                        var66 = -0.020468675
    else:
        if input[12] < 0.1300813:
            if input[11] < 0.12880678:
                if input[4] < 4562.0:
                    if input[11] < 0.11730546:
                        var66 = -0.010579045
                    else:
                        var66 = 0.011485252
                else:
                    if input[2] < 41.0:
                        var66 = -0.049372006
                    else:
                        var66 = -0.011277868
            else:
                if input[10] < 0.14522919:
                    if input[22] < 5.849868:
                        var66 = -0.012849392
                    else:
                        var66 = 0.004513682
                else:
                    if input[30] < 11.0:
                        var66 = 0.00062587234
                    else:
                        var66 = 0.0058202934
        else:
            if input[15] < 38.0:
                if input[11] < 0.2256:
                    if input[10] < 0.2961165:
                        var66 = 0.008275188
                    else:
                        var66 = 0.0051046717
                else:
                    if input[10] < 0.13035715:
                        var66 = 0.003600175
                    else:
                        var66 = 0.0068814144
            else:
                if input[11] < 0.31177828:
                    if input[25] < 0.006695871:
                        var66 = 0.010541388
                    else:
                        var66 = 0.007784512
                else:
                    if input[30] < 13.0:
                        var66 = 0.022772372
                    else:
                        var66 = 0.0014432652
    if input[15] < 30.0:
        if input[12] < 0.14899713:
            if input[35] < 17.238165:
                if input[4] < 12102.0:
                    if input[12] < 0.07342466:
                        var67 = -0.020239932
                    else:
                        var67 = -0.0012934714
                else:
                    if input[0] < 1785.0:
                        var67 = -0.04337973
                    else:
                        var67 = 0.009308684
            else:
                if input[5] < 79.0:
                    if input[7] < 54.0:
                        var67 = 0.00055806705
                    else:
                        var67 = -0.0121394545
                else:
                    if input[10] < 0.37548056:
                        var67 = 0.00399694
                    else:
                        var67 = -0.0034755785
        else:
            if input[10] < 0.14970563:
                if input[24] < 161555.0:
                    if input[19] < 153.02295:
                        var67 = 0.003916781
                    else:
                        var67 = 0.000010326679
                else:
                    if input[2] < 91.0:
                        var67 = -0.033884324
                    else:
                        var67 = 0.001903718
            else:
                if input[12] < 0.2265861:
                    if input[19] < 68.88758:
                        var67 = 0.0027553933
                    else:
                        var67 = 0.005530004
                else:
                    if input[10] < 0.25016677:
                        var67 = 0.007561106
                    else:
                        var67 = 0.0036969054
    else:
        if input[12] < 0.10612245:
            if input[22] < 6.456181:
                if input[10] < 0.16495806:
                    if input[6] < 453.0:
                        var67 = 0.011888946
                    else:
                        var67 = -0.0218176
                else:
                    if input[11] < 0.123484015:
                        var67 = -0.02189464
                    else:
                        var67 = 0.0022544393
            else:
                if input[2] < 100.0:
                    if input[7] < 1327.0:
                        var67 = 0.0060444972
                    else:
                        var67 = 0.018899988
                else:
                    if input[5] < 1085.0:
                        var67 = -0.056147195
                    else:
                        var67 = 0.006285816
        else:
            if input[12] < 0.28242075:
                if input[15] < 36.0:
                    if input[13] < 0.27929688:
                        var67 = -0.0028514029
                    else:
                        var67 = 0.0065495046
                else:
                    if input[15] < 44.0:
                        var67 = 0.007746396
                    else:
                        var67 = 0.011275928
            else:
                if input[22] < 4.8675985:
                    if input[11] < 0.1954638:
                        var67 = 0.022882042
                    else:
                        var67 = -0.015090785
                else:
                    if input[10] < 0.32578397:
                        var67 = 0.009179383
                    else:
                        var67 = -0.023234097
    if input[7] < 266.0:
        if input[30] < 18.0:
            if input[12] < 0.22083333:
                if input[5] < 73.0:
                    if input[20] < 13.659193:
                        var68 = 0.0014913442
                    else:
                        var68 = -0.008405597
                else:
                    if input[11] < 0.10509839:
                        var68 = -0.0030879162
                    else:
                        var68 = 0.004223326
            else:
                if input[11] < 0.21066667:
                    if input[16] < 26.362997:
                        var68 = 0.006758816
                    else:
                        var68 = 0.0043928726
                else:
                    if input[17] < 1075.0:
                        var68 = 0.0013088415
                    else:
                        var68 = 0.005796619
        else:
            if input[8] < 678.0:
                if input[35] < 18.95267:
                    if input[35] < 17.866903:
                        var68 = 0.0047631655
                    else:
                        var68 = 0.0076730894
                else:
                    if input[20] < 14.919574:
                        var68 = 0.010089791
                    else:
                        var68 = 0.0024298772
            else:
                if input[6] < 637.0:
                    if input[12] < 0.080063626:
                        var68 = -0.02673818
                    else:
                        var68 = -0.00074600073
                else:
                    if input[2] < 8.0:
                        var68 = -0.010331409
                    else:
                        var68 = 0.010165898
    else:
        if input[30] < 10.0:
            if input[11] < 0.07709251:
                if input[7] < 395.0:
                    var68 = -0.053426888
                else:
                    if input[16] < 26.685286:
                        var68 = 0.0079452535
                    else:
                        var68 = -0.015064159
            else:
                if input[13] < 0.44163424:
                    if input[35] < 18.859701:
                        var68 = 0.0049240175
                    else:
                        var68 = -0.000015526648
                else:
                    if input[12] < 0.26436782:
                        var68 = -0.0019276835
                    else:
                        var68 = -0.05622529
        else:
            if input[15] < 45.0:
                if input[12] < 0.12069428:
                    if input[35] < 17.109346:
                        var68 = -0.010235047
                    else:
                        var68 = 0.003419817
                else:
                    if input[11] < 0.23570432:
                        var68 = 0.0069684386
                    else:
                        var68 = 0.0055546556
            else:
                if input[4] < 3396.0:
                    if input[16] < 36.40073:
                        var68 = -0.0040308926
                    else:
                        var68 = 0.018719796
                else:
                    if input[2] < 21.0:
                        var68 = -0.0018345735
                    else:
                        var68 = 0.011264867
    if input[15] < 28.0:
        if input[11] < 0.25804585:
            if input[10] < 0.26643598:
                if input[13] < 0.40008345:
                    if input[11] < 0.20651747:
                        var69 = 0.006273787
                    else:
                        var69 = 0.0044433773
                else:
                    if input[13] < 0.46285716:
                        var69 = 0.0033948843
                    else:
                        var69 = -0.007424086
            else:
                if input[20] < 11.424528:
                    if input[6] < 157.0:
                        var69 = -0.000109740104
                    else:
                        var69 = -0.048777733
                else:
                    if input[35] < 17.74646:
                        var69 = -0.0000213474
                    else:
                        var69 = 0.003830586
        else:
            if input[24] < 111809.0:
                if input[11] < 0.30880615:
                    if input[22] < 5.5425453:
                        var69 = 0.0025630686
                    else:
                        var69 = -0.003432742
                else:
                    if input[30] < 10.0:
                        var69 = -0.0075602396
                    else:
                        var69 = -0.0004865305
            else:
                if input[11] < 0.38214287:
                    if input[22] < 4.7004967:
                        var69 = 0.0030263138
                    else:
                        var69 = 0.0097455345
                else:
                    var69 = -0.04133993
    else:
        if input[10] < 0.35:
            if input[11] < 0.2256:
                if input[35] < 17.718607:
                    if input[12] < 0.14978448:
                        var69 = 0.0015283304
                    else:
                        var69 = 0.0052354196
                else:
                    if input[15] < 33.0:
                        var69 = 0.0059716995
                    else:
                        var69 = 0.007446134
            else:
                if input[15] < 38.0:
                    if input[11] < 0.36167213:
                        var69 = 0.0045528295
                    else:
                        var69 = -0.0024802925
                else:
                    if input[10] < 0.30929792:
                        var69 = 0.007096006
                    else:
                        var69 = -0.0060857083
        else:
            if input[30] < 10.0:
                if input[22] < 5.3528438:
                    if input[15] < 29.0:
                        var69 = -0.010677326
                    else:
                        var69 = -0.058113407
                else:
                    if input[22] < 5.5963655:
                        var69 = 0.017144343
                    else:
                        var69 = -0.010515097
            else:
                if input[12] < 0.19354838:
                    if input[3] < 6346.6816:
                        var69 = 0.0025877429
                    else:
                        var69 = -0.022477375
                else:
                    if input[12] < 0.19774719:
                        var69 = -0.032471072
                    else:
                        var69 = -0.004259547
    if input[30] < 11.0:
        if input[10] < 0.3225058:
            if input[13] < 0.39285713:
                if input[35] < 18.712122:
                    if input[7] < 66.0:
                        var70 = 0.0011870317
                    else:
                        var70 = 0.0051575084
                else:
                    if input[12] < 0.32160804:
                        var70 = 0.001936151
                    else:
                        var70 = 0.008011874
            else:
                if input[15] < 28.0:
                    if input[24] < 161555.0:
                        var70 = 0.0008761187
                    else:
                        var70 = -0.016361468
                else:
                    if input[35] < 17.718607:
                        var70 = 0.0010988081
                    else:
                        var70 = 0.0065276786
        else:
            if input[22] < 5.3528438:
                if input[20] < 16.45514:
                    if input[19] < 142.5912:
                        var70 = -0.004241672
                    else:
                        var70 = 0.019597715
                else:
                    if input[7] < 1963.0:
                        var70 = -0.02991722
                    else:
                        var70 = 0.020673996
            else:
                if input[20] < 15.56671:
                    if input[7] < 49.0:
                        var70 = -0.008552114
                    else:
                        var70 = 0.026248395
                else:
                    if input[11] < 0.13636364:
                        var70 = -0.009874691
                    else:
                        var70 = 0.008380364
    else:
        if input[7] < 181.0:
            if input[13] < 0.42833108:
                if input[11] < 0.25368324:
                    if input[10] < 0.29043126:
                        var70 = 0.004810992
                    else:
                        var70 = 0.0027490864
                else:
                    if input[35] < 18.897121:
                        var70 = 0.0038834375
                    else:
                        var70 = 0.000437871
            else:
                if input[35] < 17.718607:
                    if input[10] < 0.26150122:
                        var70 = 0.0022692888
                    else:
                        var70 = -0.004427909
                else:
                    if input[0] < 1381.0:
                        var70 = -0.0062841587
                    else:
                        var70 = -0.04205888
        else:
            if input[11] < 0.33045977:
                if input[7] < 703.0:
                    if input[13] < 0.405954:
                        var70 = 0.005407587
                    else:
                        var70 = 0.0038425424
                else:
                    if input[22] < 4.322658:
                        var70 = -0.010180014
                    else:
                        var70 = 0.006594941
            else:
                if input[25] < 0.00068372575:
                    if input[11] < 0.36167213:
                        var70 = 0.00792729
                    else:
                        var70 = 0.024115345
                else:
                    if input[8] < 3888.0:
                        var70 = 0.0005835902
                    else:
                        var70 = -0.048101667
    if input[30] < 18.0:
        if input[12] < 0.16783217:
            if input[12] < 0.07342466:
                if input[24] < 42603.0:
                    if input[11] < 0.29946524:
                        var71 = -0.0020087908
                    else:
                        var71 = -0.026143743
                else:
                    if input[11] < 0.17094018:
                        var71 = -0.020166742
                    else:
                        var71 = 0.00030102415
            else:
                if input[10] < 0.1558642:
                    if input[12] < 0.08512975:
                        var71 = -0.02664787
                    else:
                        var71 = -0.0005243214
                else:
                    if input[6] < 164.0:
                        var71 = 0.0017456139
                    else:
                        var71 = 0.0035880327
        else:
            if input[5] < 115.0:
                if input[11] < 0.2875817:
                    if input[13] < 0.4027778:
                        var71 = 0.0034855746
                    else:
                        var71 = 0.0009165855
                else:
                    if input[16] < 21.584862:
                        var71 = 0.010051294
                    else:
                        var71 = -0.00447433
            else:
                if input[19] < 60.19968:
                    if input[7] < 89.0:
                        var71 = -0.05739085
                    else:
                        var71 = -0.0038842328
                else:
                    if input[10] < 0.24941905:
                        var71 = 0.0048286445
                    else:
                        var71 = 0.003152379
    else:
        if input[12] < 0.17879274:
            if input[4] < 6556.0:
                if input[11] < 0.36167213:
                    if input[15] < 40.0:
                        var71 = 0.004904132
                    else:
                        var71 = 0.009834376
                else:
                    if input[1] < 3.8481233:
                        var71 = 0.010394783
                    else:
                        var71 = -0.016361466
            else:
                if input[24] < 95499.0:
                    if input[13] < 0.3211404:
                        var71 = 0.011644357
                    else:
                        var71 = -0.00023546659
                else:
                    if input[4] < 6684.0:
                        var71 = -0.036673333
                    else:
                        var71 = 0.0051091793
        else:
            if input[16] < 44.547756:
                if input[13] < 0.3253012:
                    if input[13] < 0.32417583:
                        var71 = 0.003999688
                    else:
                        var71 = -0.01185733
                else:
                    if input[13] < 0.3802817:
                        var71 = 0.0071723773
                    else:
                        var71 = 0.0053728404
            else:
                if input[10] < 0.26498422:
                    if input[10] < 0.13652053:
                        var71 = 0.006897499
                    else:
                        var71 = 0.019148646
                else:
                    if input[10] < 0.28658536:
                        var71 = -0.008055585
                    else:
                        var71 = 0.013470413
    if input[30] < 11.0:
        if input[11] < 0.0931677:
            if input[15] < 36.0:
                if input[16] < 26.362997:
                    if input[15] < 25.0:
                        var72 = -0.009913507
                    else:
                        var72 = 0.0092126895
                else:
                    if input[26] < 9.457787:
                        var72 = 0.008769663
                    else:
                        var72 = -0.01790134
            else:
                var72 = 0.01882587
        else:
            if input[12] < 0.13118812:
                if input[1] < 5.792373:
                    if input[6] < 127.0:
                        var72 = -0.00340942
                    else:
                        var72 = 0.00541992
                else:
                    if input[22] < 6.3436112:
                        var72 = -0.0033528612
                    else:
                        var72 = 0.018870166
            else:
                if input[11] < 0.38214287:
                    if input[13] < 0.33223847:
                        var72 = 0.00064164307
                    else:
                        var72 = 0.003001103
                else:
                    if input[3] < 3680.3635:
                        var72 = -0.0050222743
                    else:
                        var72 = -0.05242153
    else:
        if input[12] < 0.24329026:
            if input[10] < 0.10747664:
                if input[26] < 170.85095:
                    if input[1] < 10.697594:
                        var72 = -0.0017809138
                    else:
                        var72 = 0.013527818
                else:
                    if input[30] < 13.0:
                        var72 = -0.037319988
                    else:
                        var72 = -0.009519747
            else:
                if input[7] < 207.0:
                    if input[6] < 503.0:
                        var72 = 0.0031228364
                    else:
                        var72 = -0.004189882
                else:
                    if input[10] < 0.37548056:
                        var72 = 0.004275712
                    else:
                        var72 = -0.0033588184
        else:
            if input[13] < 0.3153786:
                if input[22] < 4.433995:
                    if input[35] < 20.16387:
                        var72 = -0.004765188
                    else:
                        var72 = -0.044630446
                else:
                    if input[1] < 11.289093:
                        var72 = 0.002905527
                    else:
                        var72 = -0.014546931
            else:
                if input[11] < 0.08375:
                    if input[8] < 447.0:
                        var72 = -0.008366334
                    else:
                        var72 = 0.0026820207
                else:
                    if input[29] < 1115.0:
                        var72 = 0.005379514
                    else:
                        var72 = 0.0101906555
    if input[30] < 18.0:
        if input[12] < 0.23003472:
            if input[10] < 0.35:
                if input[5] < 73.0:
                    if input[6] < 104.0:
                        var73 = 0.0008579286
                    else:
                        var73 = -0.0049218712
                else:
                    if input[13] < 0.4293405:
                        var73 = 0.0030210789
                    else:
                        var73 = 0.00077512796
            else:
                if input[24] < 135403.0:
                    if input[12] < 0.18401015:
                        var73 = 0.00017517035
                    else:
                        var73 = -0.008171552
                else:
                    if input[11] < 0.17475729:
                        var73 = -0.007131041
                    else:
                        var73 = -0.051448323
        else:
            if input[10] < 0.26741394:
                if input[11] < 0.21859904:
                    if input[0] < 5632.0:
                        var73 = 0.004336722
                    else:
                        var73 = 0.008908881
                else:
                    if input[7] < 347.0:
                        var73 = 0.0006391951
                    else:
                        var73 = 0.0038077594
            else:
                if input[26] < 16.026628:
                    if input[10] < 0.2710911:
                        var73 = -0.047006752
                    else:
                        var73 = -0.0060420656
                else:
                    if input[35] < 18.5562:
                        var73 = 0.0044792825
                    else:
                        var73 = -0.00088449474
    else:
        if input[12] < 0.2877698:
            if input[13] < 0.31913877:
                if input[24] < 67647.0:
                    if input[26] < 60.927094:
                        var73 = 0.00058049447
                    else:
                        var73 = -0.017299924
                else:
                    if input[4] < 8017.0:
                        var73 = 0.007609802
                    else:
                        var73 = 0.00013159087
            else:
                if input[13] < 0.4041451:
                    if input[10] < 0.15400203:
                        var73 = 0.0022144779
                    else:
                        var73 = 0.005250659
                else:
                    if input[35] < 18.098145:
                        var73 = 0.0036748443
                    else:
                        var73 = -0.0064065405
        else:
            if input[3] < 5498.9546:
                if input[20] < 23.430506:
                    if input[26] < 197.98845:
                        var73 = 0.007302066
                    else:
                        var73 = -0.0065905997
                else:
                    if input[4] < 1621.0:
                        var73 = 0.026381522
                    else:
                        var73 = 0.0114342645
            else:
                if input[24] < 130576.0:
                    if input[16] < 37.356094:
                        var73 = -0.001923224
                    else:
                        var73 = -0.024295744
                else:
                    if input[1] < 4.5955763:
                        var73 = -0.008249783
                    else:
                        var73 = 0.011024138
    if input[30] < 12.0:
        if input[12] < 0.07342466:
            if input[35] < 18.515:
                if input[35] < 18.03752:
                    if input[10] < 0.33581847:
                        var74 = -0.0019282198
                    else:
                        var74 = -0.023212707
                else:
                    if input[3] < 4790.864:
                        var74 = -0.03313643
                    else:
                        var74 = 0.0053511197
            else:
                if input[13] < 0.32922128:
                    if input[1] < 9.172678:
                        var74 = -0.0221041
                    else:
                        var74 = 0.008613905
                else:
                    if input[11] < 0.3042328:
                        var74 = 0.022771342
                    else:
                        var74 = 0.0040694713
        else:
            if input[15] < 24.0:
                if input[11] < 0.102564104:
                    if input[5] < 299.0:
                        var74 = -0.0065557547
                    else:
                        var74 = -0.039400037
                else:
                    if input[16] < 28.171534:
                        var74 = 0.0014707132
                    else:
                        var74 = -0.04289795
            else:
                if input[16] < 25.496319:
                    if input[29] < 104.0:
                        var74 = 0.00043356558
                    else:
                        var74 = 0.0047113476
                else:
                    if input[19] < 111.80336:
                        var74 = -0.0015206035
                    else:
                        var74 = 0.0023848899
    else:
        if input[10] < 0.35:
            if input[7] < 307.0:
                if input[11] < 0.34256172:
                    if input[12] < 0.09598741:
                        var74 = -0.00056755514
                    else:
                        var74 = 0.0030901895
                else:
                    if input[7] < 254.0:
                        var74 = -0.00044993762
                    else:
                        var74 = -0.016420312
            else:
                if input[13] < 0.41821945:
                    if input[10] < 0.15306123:
                        var74 = 0.0028472026
                    else:
                        var74 = 0.004603066
                else:
                    if input[16] < 26.362997:
                        var74 = 0.0100373095
                    else:
                        var74 = 0.0021150375
        else:
            if input[12] < 0.19354838:
                if input[30] < 15.0:
                    if input[1] < 8.463247:
                        var74 = -0.006653757
                    else:
                        var74 = 0.00568417
                else:
                    if input[4] < 3739.0:
                        var74 = 0.0062737702
                    else:
                        var74 = -0.00031987205
            else:
                if input[2] < 35.0:
                    if input[3] < 1285.2632:
                        var74 = -0.013934525
                    else:
                        var74 = -0.06515259
                else:
                    if input[12] < 0.19774719:
                        var74 = -0.019020606
                    else:
                        var74 = 0.002699657
    if input[30] < 10.0:
        if input[13] < 0.41893157:
            if input[10] < 0.3394348:
                if input[11] < 0.3019608:
                    if input[25] < 1.1988763:
                        var75 = 0.0020284366
                    else:
                        var75 = -0.0031537642
                else:
                    if input[2] < 89.0:
                        var75 = -0.0052417438
                    else:
                        var75 = 0.011367622
            else:
                if input[16] < 28.224092:
                    if input[8] < 447.0:
                        var75 = -0.0057538743
                    else:
                        var75 = 0.018394617
                else:
                    if input[15] < 35.0:
                        var75 = -0.030197129
                    else:
                        var75 = 0.0049304445
        else:
            if input[1] < 2.5158632:
                if input[10] < 0.13926017:
                    var75 = 0.02484244
                else:
                    if input[15] < 20.0:
                        var75 = -0.0030259804
                    else:
                        var75 = 0.011004309
            else:
                if input[1] < 4.065793:
                    if input[1] < 3.8153753:
                        var75 = -0.0048129056
                    else:
                        var75 = -0.027209789
                else:
                    if input[12] < 0.23137744:
                        var75 = 0.00012672566
                    else:
                        var75 = -0.009199395
    else:
        if input[12] < 0.16605166:
            if input[22] < 6.613095:
                if input[10] < 0.14970563:
                    if input[11] < 0.28440368:
                        var75 = -0.013488501
                    else:
                        var75 = -0.00086271606
                else:
                    if input[11] < 0.14437367:
                        var75 = -0.0017282831
                    else:
                        var75 = 0.0020110917
            else:
                if input[35] < 17.201937:
                    if input[15] < 40.0:
                        var75 = -0.009953082
                    else:
                        var75 = 0.003994696
                else:
                    if input[15] < 45.0:
                        var75 = 0.0038414102
                    else:
                        var75 = 0.009009435
        else:
            if input[19] < 184.59396:
                if input[35] < 19.862576:
                    if input[13] < 0.45728898:
                        var75 = 0.0029465265
                    else:
                        var75 = -0.0037011083
                else:
                    if input[2] < 18.0:
                        var75 = -0.014532762
                    else:
                        var75 = -0.00070361426
            else:
                if input[22] < 4.209721:
                    if input[6] < 1325.0:
                        var75 = -0.018412638
                    else:
                        var75 = 0.0028610062
                else:
                    if input[10] < 0.07663783:
                        var75 = -0.004608422
                    else:
                        var75 = 0.004129546
    if input[30] < 18.0:
        if input[12] < 0.22401847:
            if input[30] < 10.0:
                if input[2] < 95.0:
                    if input[35] < 20.16387:
                        var76 = -0.0001311953
                    else:
                        var76 = -0.035060637
                else:
                    if input[5] < 69.0:
                        var76 = -0.0123699475
                    else:
                        var76 = 0.0077760927
            else:
                if input[10] < 0.1558642:
                    if input[12] < 0.08512975:
                        var76 = -0.020371446
                    else:
                        var76 = 0.00049283355
                else:
                    if input[11] < 0.124938026:
                        var76 = -0.00029395265
                    else:
                        var76 = 0.0022636931
        else:
            if input[11] < 0.08375:
                if input[1] < 12.150158:
                    if input[35] < 19.19658:
                        var76 = -0.001639241
                    else:
                        var76 = -0.02469328
                else:
                    var76 = -0.03075455
            else:
                if input[10] < 0.110275686:
                    if input[22] < 5.0935316:
                        var76 = -0.00445497
                    else:
                        var76 = 0.0018302726
                else:
                    if input[25] < 0.0037467263:
                        var76 = 0.0052453047
                    else:
                        var76 = 0.0028803565
    else:
        if input[20] < 25.892977:
            if input[11] < 0.20704846:
                if input[10] < 0.2710911:
                    if input[5] < 75.0:
                        var76 = -0.005415006
                    else:
                        var76 = 0.004693607
                else:
                    if input[2] < 99.0:
                        var76 = 0.0022426767
                    else:
                        var76 = 0.013079642
            else:
                if input[35] < 17.866903:
                    if input[11] < 0.21112256:
                        var76 = -0.014671259
                    else:
                        var76 = 0.00084786705
                else:
                    if input[1] < 10.076003:
                        var76 = 0.0033361316
                    else:
                        var76 = -0.0014601279
        else:
            if input[4] < 5954.0:
                if input[35] < 18.521347:
                    if input[6] < 1831.0:
                        var76 = 0.016463524
                    else:
                        var76 = 0.0008755741
                else:
                    if input[10] < 0.20269966:
                        var76 = 0.028780445
                    else:
                        var76 = 0.0128016
            else:
                if input[24] < 90351.0:
                    if input[15] < 46.0:
                        var76 = -0.022591598
                    else:
                        var76 = -0.000326024
                else:
                    if input[3] < 5349.4287:
                        var76 = 0.011374279
                    else:
                        var76 = -0.0038702793
    if input[30] < 17.0:
        if input[3] < 81.210526:
            if input[22] < 4.8675985:
                if input[19] < 134.5988:
                    if input[8] < 316.0:
                        var77 = 0.0013677995
                    else:
                        var77 = 0.010900996
                else:
                    if input[6] < 213.0:
                        var77 = -0.045487653
                    else:
                        var77 = -0.010787174
            else:
                if input[35] < 18.364511:
                    if input[29] < 335.0:
                        var77 = 0.003220111
                    else:
                        var77 = 0.017082322
                else:
                    if input[19] < 110.231415:
                        var77 = 0.015835987
                    else:
                        var77 = 0.007209744
        else:
            if input[24] < 3996.0:
                if input[4] < 236.0:
                    if input[24] < 2467.0:
                        var77 = -0.025371686
                    else:
                        var77 = -0.00008151794
                else:
                    if input[2] < 5.0:
                        var77 = -0.03256696
                    else:
                        var77 = -0.0076423693
            else:
                if input[15] < 26.0:
                    if input[10] < 0.15673469:
                        var77 = -0.0011128223
                    else:
                        var77 = 0.0014465664
                else:
                    if input[13] < 0.2934363:
                        var77 = -0.0017912565
                    else:
                        var77 = 0.0022885732
    else:
        if input[7] < 1803.0:
            if input[10] < 0.2961165:
                if input[13] < 0.40784603:
                    if input[11] < 0.31177828:
                        var77 = 0.0035375336
                    else:
                        var77 = 0.000039442235
                else:
                    if input[11] < 0.2053942:
                        var77 = 0.00295621
                    else:
                        var77 = -0.0002506637
            else:
                if input[35] < 19.480465:
                    if input[3] < 758.7619:
                        var77 = -0.0027630306
                    else:
                        var77 = 0.002291697
                else:
                    if input[7] < 765.0:
                        var77 = -0.0052682674
                    else:
                        var77 = -0.026005426
        else:
            if input[13] < 0.34612104:
                if input[1] < 10.076003:
                    if input[35] < 18.976562:
                        var77 = 0.018495899
                    else:
                        var77 = 0.008680179
                else:
                    var77 = -0.021492723
            else:
                if input[35] < 18.635206:
                    if input[10] < 0.21333334:
                        var77 = 0.00790676
                    else:
                        var77 = 0.0020999124
                else:
                    if input[13] < 0.36949152:
                        var77 = -0.0053523458
                    else:
                        var77 = -0.053588778
    if input[15] < 34.0:
        if input[12] < 0.14516129:
            if input[11] < 0.36167213:
                if input[11] < 0.13968255:
                    if input[30] < 12.0:
                        var78 = 0.001047751
                    else:
                        var78 = -0.008298209
                else:
                    if input[19] < 50.294167:
                        var78 = -0.0062666624
                    else:
                        var78 = 0.0010101008
            else:
                if input[13] < 0.3897243:
                    if input[0] < 753.0:
                        var78 = -0.013421719
                    else:
                        var78 = 0.00080770784
                else:
                    if input[16] < 25.715717:
                        var78 = -0.00069470395
                    else:
                        var78 = -0.04159322
        else:
            if input[5] < 1403.0:
                if input[35] < 19.862576:
                    if input[13] < 0.46285716:
                        var78 = 0.0020709939
                    else:
                        var78 = -0.0049970723
                else:
                    if input[26] < 21.093458:
                        var78 = -0.011220436
                    else:
                        var78 = -0.00079594814
            else:
                if input[0] < 5872.0:
                    if input[13] < 0.39966834:
                        var78 = -0.016368765
                    else:
                        var78 = -0.05810801
                else:
                    if input[20] < 21.173801:
                        var78 = 0.0006330295
                    else:
                        var78 = -0.028832857
    else:
        if input[12] < 0.080063626:
            if input[22] < 5.8051906:
                if input[11] < 0.16016074:
                    var78 = 0.02277208
                else:
                    if input[13] < 0.43141693:
                        var78 = -0.037814163
                    else:
                        var78 = 0.007463912
            else:
                if input[4] < 2734.0:
                    if input[30] < 17.0:
                        var78 = -0.031781234
                    else:
                        var78 = -0.0040240264
                else:
                    if input[3] < 5573.3184:
                        var78 = 0.004737937
                    else:
                        var78 = -0.01729779
        else:
            if input[4] < 764.0:
                if input[13] < 0.3153786:
                    if input[0] < 4796.0:
                        var78 = -0.00095620705
                    else:
                        var78 = -0.04809616
                else:
                    if input[7] < 1212.0:
                        var78 = 0.005813266
                    else:
                        var78 = 0.019247556
            else:
                if input[24] < 9736.0:
                    if input[15] < 38.0:
                        var78 = -0.05696177
                    else:
                        var78 = -0.015370751
                else:
                    if input[5] < 309.0:
                        var78 = 0.0012505017
                    else:
                        var78 = 0.0030209397
    if input[30] < 10.0:
        if input[11] < 0.102564104:
            if input[4] < 10674.0:
                if input[2] < 56.0:
                    if input[4] < 5595.0:
                        var79 = -0.00431738
                    else:
                        var79 = -0.033471446
                else:
                    if input[12] < 0.14594595:
                        var79 = -0.020753125
                    else:
                        var79 = 0.005482406
            else:
                if input[12] < 0.19178082:
                    var79 = 0.007936166
                else:
                    if input[3] < 6042.5454:
                        var79 = -0.015199274
                    else:
                        var79 = -0.046382762
        else:
            if input[12] < 0.22147302:
                if input[2] < 95.0:
                    if input[2] < 56.0:
                        var79 = 0.0006523758
                    else:
                        var79 = -0.0023254778
                else:
                    if input[12] < 0.098779134:
                        var79 = -0.026291057
                    else:
                        var79 = 0.005944812
            else:
                if input[13] < 0.41955444:
                    if input[35] < 18.683113:
                        var79 = 0.004083522
                    else:
                        var79 = -0.0000868588
                else:
                    if input[10] < 0.11335337:
                        var79 = -0.022027394
                    else:
                        var79 = -0.0013642926
    else:
        if input[12] < 0.24329026:
            if input[0] < 746.0:
                if input[6] < 203.0:
                    if input[10] < 0.18523775:
                        var79 = -0.0008347514
                    else:
                        var79 = 0.0013836836
                else:
                    if input[22] < 6.7334175:
                        var79 = -0.004314851
                    else:
                        var79 = -0.030853933
            else:
                if input[13] < 0.39444613:
                    if input[35] < 19.059431:
                        var79 = 0.0025702105
                    else:
                        var79 = 0.0008718581
                else:
                    if input[12] < 0.17261904:
                        var79 = 0.00032017718
                    else:
                        var79 = 0.0020509604
        else:
            if input[10] < 0.2777778:
                if input[25] < 0.00030379987:
                    if input[10] < 0.24136178:
                        var79 = 0.008794479
                    else:
                        var79 = 0.023648446
                else:
                    if input[35] < 19.862576:
                        var79 = 0.0029406268
                    else:
                        var79 = -0.002865089
            else:
                if input[10] < 0.28091604:
                    if input[8] < 372.0:
                        var79 = -0.002016737
                    else:
                        var79 = -0.02205195
                else:
                    if input[22] < 5.1604013:
                        var79 = 0.0047443504
                    else:
                        var79 = -0.003320902
    if input[30] < 18.0:
        if input[10] < 0.31991714:
            if input[3] < 81.210526:
                if input[6] < 119.0:
                    if input[6] < 112.0:
                        var80 = 0.0028724957
                    else:
                        var80 = -0.019500196
                else:
                    if input[25] < 0.0023812808:
                        var80 = 0.0052461396
                    else:
                        var80 = 0.011737305
            else:
                if input[11] < 0.24369748:
                    if input[35] < 17.598156:
                        var80 = 0.00025601842
                    else:
                        var80 = 0.0019304457
                else:
                    if input[24] < 3235.0:
                        var80 = -0.021114394
                    else:
                        var80 = 0.00069649046
        else:
            if input[2] < 6.0:
                if input[11] < 0.18209212:
                    if input[3] < 37.38889:
                        var80 = 0.010663435
                    else:
                        var80 = -0.011382141
                else:
                    if input[10] < 0.34461153:
                        var80 = -0.054163434
                    else:
                        var80 = -0.0122908745
            else:
                if input[12] < 0.24758221:
                    if input[22] < 3.5597324:
                        var80 = -0.011609283
                    else:
                        var80 = 0.00012281144
                else:
                    if input[11] < 0.07709251:
                        var80 = -0.030750856
                    else:
                        var80 = -0.006670763
    else:
        if input[1] < 2.447644:
            if input[22] < 7.5069256:
                if input[35] < 18.02482:
                    if input[35] < 17.499226:
                        var80 = -0.007329651
                    else:
                        var80 = 0.012692002
                else:
                    if input[22] < 6.941912:
                        var80 = 0.0043130796
                    else:
                        var80 = -0.0085624
            else:
                if input[11] < 0.19193427:
                    if input[10] < 0.16658017:
                        var80 = -0.002240575
                    else:
                        var80 = 0.01007801
                else:
                    if input[3] < 1738.6666:
                        var80 = 0.01923452
                    else:
                        var80 = 0.0027193509
        else:
            if input[26] < 2.9937801:
                if input[35] < 18.515:
                    if input[22] < 7.0782166:
                        var80 = -0.009047156
                    else:
                        var80 = 0.009139247
                else:
                    if input[2] < 16.0:
                        var80 = -0.0107429605
                    else:
                        var80 = -0.04844807
            else:
                if input[10] < 0.2961165:
                    if input[1] < 10.697594:
                        var80 = 0.0027401557
                    else:
                        var80 = -0.0010903082
                else:
                    if input[3] < 758.7619:
                        var80 = -0.008033298
                    else:
                        var80 = 0.0016736707
    if input[12] < 0.09598741:
        if input[15] < 39.0:
            if input[8] < 2298.0:
                if input[1] < 4.0369134:
                    if input[11] < 0.22365038:
                        var81 = -0.005911562
                    else:
                        var81 = 0.007307583
                else:
                    if input[10] < 0.1463964:
                        var81 = -0.022988463
                    else:
                        var81 = -0.0018540215
            else:
                if input[7] < 642.0:
                    if input[2] < 75.0:
                        var81 = -0.035099518
                    else:
                        var81 = 0.0015651205
                else:
                    if input[20] < 20.405575:
                        var81 = -0.017641483
                    else:
                        var81 = 0.00026944905
        else:
            if input[33] < 60127.0:
                if input[0] < 2313.0:
                    if input[4] < 7148.0:
                        var81 = 0.0017454186
                    else:
                        var81 = -0.01632356
                else:
                    if input[7] < 95.0:
                        var81 = 0.0052047
                    else:
                        var81 = 0.024675865
            else:
                if input[5] < 1227.0:
                    if input[30] < 19.0:
                        var81 = -0.0017426389
                    else:
                        var81 = -0.028970188
                else:
                    if input[13] < 0.45012164:
                        var81 = 0.007917398
                    else:
                        var81 = -0.021518316
    else:
        if input[15] < 30.0:
            if input[20] < 17.745762:
                if input[10] < 0.14970563:
                    if input[19] < 153.02295:
                        var81 = 0.00016785176
                    else:
                        var81 = -0.003996008
                else:
                    if input[12] < 0.2265861:
                        var81 = 0.0010293815
                    else:
                        var81 = 0.0022251157
            else:
                if input[13] < 0.3508772:
                    if input[1] < 3.7526042:
                        var81 = -0.027423495
                    else:
                        var81 = 0.0067017362
                else:
                    if input[1] < 1.6584686:
                        var81 = 0.018698718
                    else:
                        var81 = -0.0070800274
        else:
            if input[16] < 25.600283:
                if input[15] < 32.0:
                    if input[11] < 0.115555555:
                        var81 = 0.020825451
                    else:
                        var81 = 0.006989617
                else:
                    if input[6] < 87.0:
                        var81 = -0.011379235
                    else:
                        var81 = 0.0018008149
            else:
                if input[12] < 0.28242075:
                    if input[10] < 0.07663783:
                        var81 = -0.0065560914
                    else:
                        var81 = 0.0017527873
                else:
                    if input[22] < 4.8675985:
                        var81 = 0.012999931
                    else:
                        var81 = 0.0030727373
    if input[30] < 10.0:
        if input[11] < 0.102564104:
            if input[4] < 10674.0:
                if input[2] < 56.0:
                    if input[4] < 5595.0:
                        var82 = -0.0040712017
                    else:
                        var82 = -0.029801074
                else:
                    if input[12] < 0.14594595:
                        var82 = -0.019050859
                    else:
                        var82 = 0.004653345
            else:
                if input[12] < 0.19178082:
                    var82 = 0.0073516006
                else:
                    if input[3] < 6042.5454:
                        var82 = -0.013838964
                    else:
                        var82 = -0.041954983
        else:
            if input[11] < 0.3019608:
                if input[13] < 0.41893157:
                    if input[4] < 1812.0:
                        var82 = -0.0020782833
                    else:
                        var82 = 0.0012387567
                else:
                    if input[1] < 2.5158632:
                        var82 = 0.012349673
                    else:
                        var82 = -0.0026685996
            else:
                if input[2] < 89.0:
                    if input[3] < 4740.636:
                        var82 = -0.004038567
                    else:
                        var82 = -0.028297096
                else:
                    if input[5] < 147.0:
                        var82 = 0.020943573
                    else:
                        var82 = -0.005594428
    else:
        if input[10] < 0.27865613:
            if input[11] < 0.18328841:
                if input[25] < 0.00030379987:
                    if input[10] < 0.27670753:
                        var82 = 0.010968504
                    else:
                        var82 = -0.016396763
                else:
                    if input[5] < 49.0:
                        var82 = -0.0073444988
                    else:
                        var82 = 0.0023254005
            else:
                if input[29] < 352.0:
                    if input[13] < 0.47155812:
                        var82 = 0.0009197641
                    else:
                        var82 = -0.015587873
                else:
                    if input[5] < 400.0:
                        var82 = 0.0053504487
                    else:
                        var82 = 0.0014915811
        else:
            if input[35] < 17.74646:
                if input[2] < 87.0:
                    if input[1] < 5.8154483:
                        var82 = -0.00039542792
                    else:
                        var82 = -0.004700456
                else:
                    if input[6] < 242.0:
                        var82 = -0.00066145096
                    else:
                        var82 = 0.008168901
            else:
                if input[22] < 3.8806787:
                    if input[35] < 18.548388:
                        var82 = 0.0005163346
                    else:
                        var82 = -0.015628971
                else:
                    if input[11] < 0.2656396:
                        var82 = 0.0012763494
                    else:
                        var82 = -0.003881108
    if input[10] < 0.35:
        if input[30] < 14.0:
            if input[2] < 10.0:
                if input[10] < 0.32578397:
                    if input[22] < 6.4267254:
                        var83 = 0.0029885916
                    else:
                        var83 = 0.011284864
                else:
                    if input[11] < 0.15181269:
                        var83 = 0.0028660335
                    else:
                        var83 = -0.027571535
            else:
                if input[11] < 0.3178114:
                    if input[10] < 0.24009325:
                        var83 = 0.0011226434
                    else:
                        var83 = 0.00004549163
                else:
                    if input[13] < 0.36910197:
                        var83 = 0.00027063204
                    else:
                        var83 = -0.007142848
        else:
            if input[13] < 0.42390525:
                if input[11] < 0.21907601:
                    if input[6] < 246.0:
                        var83 = 0.0015533554
                    else:
                        var83 = 0.0026836907
                else:
                    if input[16] < 21.78718:
                        var83 = -0.004978134
                    else:
                        var83 = 0.001242733
            else:
                if input[6] < 616.0:
                    if input[11] < 0.20884658:
                        var83 = 0.00025811745
                    else:
                        var83 = -0.003288071
                else:
                    if input[20] < 19.35792:
                        var83 = 0.007664261
                    else:
                        var83 = 0.0009830131
    else:
        if input[12] < 0.19414414:
            if input[24] < 86186.0:
                if input[19] < 238.91722:
                    if input[0] < 2850.0:
                        var83 = 0.0007634077
                    else:
                        var83 = 0.017246444
                else:
                    if input[19] < 243.38016:
                        var83 = -0.0435513
                    else:
                        var83 = -0.0037721817
            else:
                if input[12] < 0.15820895:
                    if input[12] < 0.1473772:
                        var83 = -0.0045996397
                    else:
                        var83 = -0.022396684
                else:
                    if input[2] < 91.0:
                        var83 = 0.008030082
                    else:
                        var83 = -0.0039677164
        else:
            if input[12] < 0.19774719:
                if input[22] < 6.4842277:
                    if input[2] < 61.0:
                        var83 = -0.04959214
                    else:
                        var83 = -0.011454033
                else:
                    if input[2] < 18.0:
                        var83 = 0.004847751
                    else:
                        var83 = -0.0073061134
            else:
                if input[26] < 84.26858:
                    if input[11] < 0.06720161:
                        var83 = 0.010021161
                    else:
                        var83 = -0.009059015
                else:
                    if input[1] < 4.145958:
                        var83 = -0.0045023663
                    else:
                        var83 = 0.015161
    if input[30] < 18.0:
        if input[35] < 17.271885:
            if input[13] < 0.4398977:
                if input[12] < 0.08949079:
                    if input[2] < 62.0:
                        var84 = 0.0044869254
                    else:
                        var84 = 0.01657132
                else:
                    if input[12] < 0.10612245:
                        var84 = -0.025883308
                    else:
                        var84 = -0.0052465126
            else:
                if input[7] < 29.0:
                    var84 = -0.029016813
                else:
                    if input[4] < 337.0:
                        var84 = 0.014990156
                    else:
                        var84 = -0.00030416934
        else:
            if input[11] < 0.33045977:
                if input[12] < 0.08512975:
                    if input[6] < 1214.0:
                        var84 = -0.0010712185
                    else:
                        var84 = -0.013965564
                else:
                    if input[13] < 0.30356118:
                        var84 = -0.0008584582
                    else:
                        var84 = 0.0011225881
            else:
                if input[35] < 18.11701:
                    if input[3] < 1100.9048:
                        var84 = 0.005947552
                    else:
                        var84 = -0.036834735
                else:
                    if input[13] < 0.4144621:
                        var84 = -0.0014903651
                    else:
                        var84 = 0.015092611
    else:
        if input[16] < 44.547756:
            if input[19] < 583.9337:
                if input[1] < 6.83554:
                    if input[1] < 6.4869747:
                        var84 = 0.0018968629
                    else:
                        var84 = 0.004967726
                else:
                    if input[4] < 3781.0:
                        var84 = 0.0038376593
                    else:
                        var84 = 0.0005731561
            else:
                if input[4] < 10462.0:
                    if input[22] < 7.2779803:
                        var84 = -0.006312325
                    else:
                        var84 = -0.04548864
                else:
                    if input[1] < 5.43827:
                        var84 = 0.011821184
                    else:
                        var84 = 0.00056280836
        else:
            if input[7] < 1327.0:
                if input[12] < 0.19014627:
                    if input[24] < 87334.0:
                        var84 = -0.030996934
                    else:
                        var84 = 0.00081391603
                else:
                    if input[13] < 0.32627118:
                        var84 = 0.016710622
                    else:
                        var84 = 0.0039854157
            else:
                if input[11] < 0.27228683:
                    if input[4] < 4355.0:
                        var84 = 0.015492702
                    else:
                        var84 = 0.0034440176
                else:
                    if input[3] < 4819.3184:
                        var84 = 0.023236249
                    else:
                        var84 = 0.006172992
    if input[30] < 10.0:
        if input[33] < 169076.0:
            if input[19] < 340.42465:
                if input[3] < 6042.5454:
                    if input[3] < 5616.591:
                        var85 = -0.00025716223
                    else:
                        var85 = 0.0071497755
                else:
                    if input[20] < 10.14724:
                        var85 = 0.012311316
                    else:
                        var85 = -0.008443017
            else:
                if input[15] < 34.0:
                    var85 = -0.010058165
                else:
                    var85 = -0.05306496
        else:
            if input[4] < 10530.0:
                if input[19] < 304.4012:
                    var85 = -0.022376671
                else:
                    if input[0] < 18475.0:
                        var85 = 0.021217445
                    else:
                        var85 = -0.01648376
            else:
                if input[1] < 7.353603:
                    if input[25] < 0.00068372575:
                        var85 = -0.028273553
                    else:
                        var85 = -0.00964284
                else:
                    if input[0] < 11593.0:
                        var85 = 0.0069013583
                    else:
                        var85 = 0.0012214076
    else:
        if input[12] < 0.26113904:
            if input[10] < 0.15306123:
                if input[1] < 10.813974:
                    if input[22] < 7.3555303:
                        var85 = -0.0008204532
                    else:
                        var85 = 0.0038928303
                else:
                    if input[2] < 99.0:
                        var85 = 0.008877528
                    else:
                        var85 = -0.018104684
            else:
                if input[13] < 0.30356118:
                    if input[5] < 363.0:
                        var85 = -0.0033076953
                    else:
                        var85 = 0.0012987107
                else:
                    if input[13] < 0.405954:
                        var85 = 0.0013118178
                    else:
                        var85 = 0.00039597586
        else:
            if input[26] < 7.902406:
                if input[10] < 0.110275686:
                    if input[11] < 0.21616541:
                        var85 = -0.011764713
                    else:
                        var85 = 0.0017851604
                else:
                    if input[35] < 19.599268:
                        var85 = 0.006351934
                    else:
                        var85 = -0.0024920206
            else:
                if input[11] < 0.08375:
                    if input[4] < 11689.0:
                        var85 = -0.004873733
                    else:
                        var85 = 0.012126103
                else:
                    if input[19] < 458.39038:
                        var85 = 0.0017548818
                    else:
                        var85 = -0.012570338
    if input[10] < 0.35:
        if input[5] < 108.0:
            if input[20] < 13.557312:
                if input[30] < 17.0:
                    if input[4] < 11144.0:
                        var86 = 0.000088772766
                    else:
                        var86 = 0.0033714378
                else:
                    if input[2] < 84.0:
                        var86 = 0.00308354
                    else:
                        var86 = 0.013653788
            else:
                if input[22] < 4.5699797:
                    if input[6] < 127.0:
                        var86 = -0.024457997
                    else:
                        var86 = -0.002893024
                else:
                    if input[4] < 8706.0:
                        var86 = -0.0001256315
                    else:
                        var86 = -0.004156634
        else:
            if input[23] < 350.0:
                var86 = -0.043516744
            else:
                if input[13] < 0.39241052:
                    if input[13] < 0.35739437:
                        var86 = 0.00077673513
                    else:
                        var86 = 0.0017690432
                else:
                    if input[7] < 1212.0:
                        var86 = 0.00033615335
                    else:
                        var86 = 0.003339144
    else:
        if input[12] < 0.18775101:
            if input[4] < 7772.0:
                if input[22] < 3.7963536:
                    if input[12] < 0.13118812:
                        var86 = -0.0011861629
                    else:
                        var86 = -0.023960996
                else:
                    if input[6] < 658.0:
                        var86 = 0.0017115775
                    else:
                        var86 = -0.0056416737
            else:
                if input[35] < 17.109346:
                    var86 = -0.04426519
                else:
                    if input[13] < 0.2934363:
                        var86 = -0.019282054
                    else:
                        var86 = -0.0023503865
        else:
            if input[24] < 78196.0:
                if input[22] < 6.6296387:
                    if input[22] < 6.329843:
                        var86 = -0.0112687
                    else:
                        var86 = -0.035859387
                else:
                    if input[22] < 6.876038:
                        var86 = 0.012054753
                    else:
                        var86 = -0.014087482
            else:
                if input[10] < 0.35634327:
                    if input[2] < 84.0:
                        var86 = 0.017128054
                    else:
                        var86 = 0.000111265224
                else:
                    if input[11] < 0.09953704:
                        var86 = 0.004993886
                    else:
                        var86 = -0.015338115
    if input[10] < 0.27865613:
        if input[11] < 0.18089172:
            if input[11] < 0.12060302:
                if input[26] < 7.3177457:
                    if input[22] < 5.9708714:
                        var87 = 0.0002262293
                    else:
                        var87 = 0.00942463
                else:
                    if input[19] < 43.5507:
                        var87 = -0.030117933
                    else:
                        var87 = -0.0005178902
            else:
                if input[7] < 651.0:
                    if input[0] < 2429.0:
                        var87 = 0.0018364455
                    else:
                        var87 = -0.0021377741
                else:
                    if input[20] < 18.558805:
                        var87 = 0.0058406214
                    else:
                        var87 = 0.002139305
        else:
            if input[22] < 4.354329:
                if input[19] < 80.8366:
                    if input[6] < 162.0:
                        var87 = 0.00037419246
                    else:
                        var87 = 0.009195867
                else:
                    if input[19] < 81.44889:
                        var87 = -0.017563373
                    else:
                        var87 = -0.0019005539
            else:
                if input[35] < 16.951084:
                    if input[4] < 3921.0:
                        var87 = -0.033575
                    else:
                        var87 = -0.0051891017
                else:
                    if input[19] < 67.94796:
                        var87 = -0.0019479608
                    else:
                        var87 = 0.0008221646
    else:
        if input[15] < 33.0:
            if input[19] < 281.8234:
                if input[11] < 0.19854721:
                    if input[2] < 86.0:
                        var87 = -0.0014877504
                    else:
                        var87 = 0.0017719277
                else:
                    if input[22] < 3.8389022:
                        var87 = -0.010225628
                    else:
                        var87 = 0.0020739574
            else:
                if input[26] < 19.367033:
                    if input[1] < 9.026796:
                        var87 = -0.0189621
                    else:
                        var87 = 0.0071194232
                else:
                    if input[7] < 839.0:
                        var87 = -0.016642509
                    else:
                        var87 = -0.053506084
        else:
            if input[6] < 854.0:
                if input[35] < 19.862576:
                    if input[22] < 7.0782166:
                        var87 = 0.0032452985
                    else:
                        var87 = -0.00008335184
                else:
                    if input[8] < 300.0:
                        var87 = -0.047619212
                    else:
                        var87 = -0.0069456147
            else:
                if input[16] < 38.44282:
                    if input[19] < 360.36847:
                        var87 = -0.003041659
                    else:
                        var87 = -0.0136694135
                else:
                    if input[20] < 22.337288:
                        var87 = 0.008461244
                    else:
                        var87 = -0.000472
    if input[3] < 81.210526:
        if input[17] < 3350.0:
            if input[22] < 7.0782166:
                if input[10] < 0.3643846:
                    if input[12] < 0.10382322:
                        var88 = 0.013252163
                    else:
                        var88 = 0.002536184
                else:
                    var88 = -0.019133732
            else:
                if input[5] < 366.0:
                    if input[25] < 0.0020526187:
                        var88 = 0.017486095
                    else:
                        var88 = 0.005261274
                else:
                    if input[4] < 136.0:
                        var88 = -0.0034732146
                    else:
                        var88 = 0.0038272613
        else:
            if input[5] < 524.0:
                if input[29] < 345.0:
                    var88 = 0.0064789774
                else:
                    var88 = 0.02318643
            else:
                var88 = 0.0051810914
    else:
        if input[24] < 3996.0:
            if input[4] < 236.0:
                if input[12] < 0.20179372:
                    if input[24] < 2467.0:
                        var88 = -0.03744344
                    else:
                        var88 = -0.0052958177
                else:
                    if input[17] < 3621.0:
                        var88 = 0.0017366965
                    else:
                        var88 = 0.021400027
            else:
                if input[5] < 210.0:
                    if input[3] < 101.65:
                        var88 = 0.0063934885
                    else:
                        var88 = -0.030142387
                else:
                    if input[22] < 6.8544707:
                        var88 = -0.027491141
                    else:
                        var88 = 0.0034857013
        else:
            if input[15] < 26.0:
                if input[10] < 0.15673469:
                    if input[25] < 0.004326864:
                        var88 = -0.030384151
                    else:
                        var88 = -0.0015482333
                else:
                    if input[20] < 16.96525:
                        var88 = 0.00038033046
                    else:
                        var88 = -0.035158228
            else:
                if input[20] < 14.527063:
                    if input[19] < 110.707466:
                        var88 = 0.0014619207
                    else:
                        var88 = 0.004979136
                else:
                    if input[22] < 4.189326:
                        var88 = -0.00829844
                    else:
                        var88 = 0.00072604365
    if input[12] < 0.09598741:
        if input[15] < 39.0:
            if input[8] < 2298.0:
                if input[1] < 4.0369134:
                    if input[11] < 0.22365038:
                        var89 = -0.0055466457
                    else:
                        var89 = 0.0061823535
                else:
                    if input[10] < 0.1463964:
                        var89 = -0.020185744
                    else:
                        var89 = -0.0019913213
            else:
                if input[7] < 642.0:
                    if input[2] < 75.0:
                        var89 = -0.03010956
                    else:
                        var89 = 0.0013996955
                else:
                    if input[30] < 15.0:
                        var89 = 0.001305411
                    else:
                        var89 = -0.015581968
        else:
            if input[13] < 0.40233237:
                if input[13] < 0.39444613:
                    if input[4] < 2146.0:
                        var89 = -0.007909616
                    else:
                        var89 = 0.0050126044
                else:
                    if input[4] < 4355.0:
                        var89 = -0.0015802985
                    else:
                        var89 = -0.025008684
            else:
                if input[1] < 7.7323194:
                    if input[5] < 2562.0:
                        var89 = 0.018281195
                    else:
                        var89 = 0.0021809526
                else:
                    if input[10] < 0.2831126:
                        var89 = -0.019480964
                    else:
                        var89 = 0.013939465
    else:
        if input[11] < 0.33045977:
            if input[3] < 37.38889:
                if input[6] < 119.0:
                    if input[25] < 0.006695871:
                        var89 = -0.00037571948
                    else:
                        var89 = 0.012313767
                else:
                    if input[12] < 0.12776025:
                        var89 = -0.013102569
                    else:
                        var89 = 0.0105381925
            else:
                if input[15] < 36.0:
                    if input[13] < 0.39241052:
                        var89 = 0.00082753814
                    else:
                        var89 = 0.000062924475
                else:
                    if input[19] < 135.2604:
                        var89 = -0.0072266483
                    else:
                        var89 = 0.0015626792
        else:
            if input[8] < 261.0:
                if input[8] < 240.0:
                    if input[16] < 28.469803:
                        var89 = -0.0018123736
                    else:
                        var89 = -0.018656397
                else:
                    if input[16] < 27.034433:
                        var89 = -0.04152674
                    else:
                        var89 = -0.001310421
            else:
                if input[10] < 0.10353011:
                    if input[26] < 31.340298:
                        var89 = -0.014362319
                    else:
                        var89 = 0.0050494573
                else:
                    if input[4] < 2614.0:
                        var89 = 0.005561313
                    else:
                        var89 = -0.00074727257
    if input[10] < 0.27865613:
        if input[11] < 0.20651747:
            if input[1] < 9.543416:
                if input[0] < 5632.0:
                    if input[16] < 17.243782:
                        var90 = -0.006925858
                    else:
                        var90 = 0.0011937944
                else:
                    if input[4] < 11797.0:
                        var90 = 0.004159361
                    else:
                        var90 = -0.0068384386
            else:
                if input[10] < 0.12306531:
                    if input[15] < 25.0:
                        var90 = -0.042949762
                    else:
                        var90 = -0.006439028
                else:
                    if input[10] < 0.22151224:
                        var90 = 0.0017117037
                    else:
                        var90 = -0.0022262153
        else:
            if input[13] < 0.4074074:
                if input[10] < 0.1252372:
                    if input[7] < 66.0:
                        var90 = -0.03164582
                    else:
                        var90 = -0.0010782364
                else:
                    if input[15] < 28.0:
                        var90 = 0.00004852477
                    else:
                        var90 = 0.0010392354
            else:
                if input[15] < 36.0:
                    if input[16] < 31.267494:
                        var90 = -0.001113137
                    else:
                        var90 = -0.0047828197
                else:
                    if input[13] < 0.41504306:
                        var90 = -0.0039251214
                    else:
                        var90 = 0.0034303423
    else:
        if input[13] < 0.42833108:
            if input[15] < 33.0:
                if input[19] < 281.8234:
                    if input[11] < 0.19377568:
                        var90 = -0.0009371224
                    else:
                        var90 = 0.0011857124
                else:
                    if input[26] < 19.367033:
                        var90 = -0.013278969
                    else:
                        var90 = -0.040557567
            else:
                if input[6] < 920.0:
                    if input[35] < 19.862576:
                        var90 = 0.0021650523
                    else:
                        var90 = -0.013684066
                else:
                    if input[8] < 2059.0:
                        var90 = -0.007408549
                    else:
                        var90 = 0.0004793956
        else:
            if input[35] < 17.3022:
                if input[1] < 9.431322:
                    if input[22] < 6.1650395:
                        var90 = -0.0014952347
                    else:
                        var90 = -0.009466175
                else:
                    if input[15] < 27.0:
                        var90 = -0.02043461
                    else:
                        var90 = 0.012729542
            else:
                if input[22] < 5.005065:
                    var90 = -0.0066637597
                else:
                    var90 = -0.036736
    if input[11] < 0.08375:
        if input[2] < 41.0:
            if input[4] < 4396.0:
                if input[12] < 0.33746272:
                    if input[6] < 58.0:
                        var91 = -0.008062049
                    else:
                        var91 = 0.0017245669
                else:
                    if input[4] < 898.0:
                        var91 = 0.0020314066
                    else:
                        var91 = -0.02586156
            else:
                if input[16] < 36.40073:
                    if input[4] < 4815.0:
                        var91 = -0.028841479
                    else:
                        var91 = -0.004747361
                else:
                    if input[13] < 0.36070383:
                        var91 = -0.08172616
                    else:
                        var91 = -0.015780343
        else:
            if input[7] < 519.0:
                if input[35] < 18.1043:
                    if input[1] < 8.135564:
                        var91 = 0.002705174
                    else:
                        var91 = -0.007330764
                else:
                    if input[13] < 0.2960822:
                        var91 = 0.0072316374
                    else:
                        var91 = -0.013132135
            else:
                if input[35] < 16.79554:
                    if input[3] < 5052.3184:
                        var91 = 0.021940766
                    else:
                        var91 = 0.008177522
                else:
                    if input[13] < 0.37594503:
                        var91 = 0.008812311
                    else:
                        var91 = -0.0023252992
    else:
        if input[12] < 0.24329026:
            if input[30] < 16.0:
                if input[11] < 0.124938026:
                    if input[8] < 316.0:
                        var91 = 0.0012769302
                    else:
                        var91 = -0.0033024487
                else:
                    if input[19] < 43.5507:
                        var91 = -0.005460931
                    else:
                        var91 = 0.00024965868
            else:
                if input[10] < 0.17336395:
                    if input[13] < 0.2986111:
                        var91 = 0.010868986
                    else:
                        var91 = -0.00081229955
                else:
                    if input[10] < 0.37548056:
                        var91 = 0.0011671998
                    else:
                        var91 = -0.005654545
        else:
            if input[13] < 0.3153786:
                if input[35] < 19.100538:
                    if input[4] < 5070.0:
                        var91 = -0.0212359
                    else:
                        var91 = -0.0052419286
                else:
                    if input[10] < 0.110275686:
                        var91 = -0.011091018
                    else:
                        var91 = -0.00011957857
            else:
                if input[19] < 181.36148:
                    if input[20] < 16.699358:
                        var91 = 0.0013394154
                    else:
                        var91 = -0.0012355432
                else:
                    if input[10] < 0.07663783:
                        var91 = -0.0067972117
                    else:
                        var91 = 0.002717553
    if input[15] < 45.0:
        if input[12] < 0.08512975:
            if input[10] < 0.1463964:
                if input[1] < 5.838965:
                    if input[1] < 4.5170293:
                        var92 = -0.015530047
                    else:
                        var92 = 0.022731777
                else:
                    if input[0] < 1173.0:
                        var92 = -0.014074047
                    else:
                        var92 = -0.049695827
            else:
                if input[11] < 0.34256172:
                    if input[6] < 1214.0:
                        var92 = -0.0013815885
                    else:
                        var92 = -0.009133159
                else:
                    if input[15] < 24.0:
                        var92 = -0.016078183
                    else:
                        var92 = 0.0077662724
        else:
            if input[11] < 0.34256172:
                if input[4] < 86.0:
                    if input[6] < 161.0:
                        var92 = 0.0025347015
                    else:
                        var92 = 0.0112658
                else:
                    if input[11] < 0.12060302:
                        var92 = -0.0005541518
                    else:
                        var92 = 0.0005547559
            else:
                if input[1] < 7.9223404:
                    if input[3] < 3591.8096:
                        var92 = -0.0024870585
                    else:
                        var92 = 0.0040528416
                else:
                    if input[26] < 57.339706:
                        var92 = -0.002444425
                    else:
                        var92 = -0.020050623
    else:
        if input[19] < 387.07837:
            if input[20] < 21.302843:
                if input[0] < 2339.0:
                    var92 = 0.005695374
                else:
                    var92 = -0.023064708
            else:
                if input[12] < 0.2320377:
                    if input[20] < 24.83409:
                        var92 = 0.012444864
                    else:
                        var92 = -0.0018028703
                else:
                    if input[35] < 17.880209:
                        var92 = -0.009588234
                    else:
                        var92 = 0.006358452
        else:
            if input[35] < 18.259357:
                if input[24] < 107337.0:
                    if input[10] < 0.29043126:
                        var92 = -0.0076762997
                    else:
                        var92 = 0.007635839
                else:
                    if input[13] < 0.38732994:
                        var92 = -0.0072940732
                    else:
                        var92 = 0.009018166
            else:
                if input[10] < 0.13652053:
                    if input[22] < 7.400384:
                        var92 = -0.02185793
                    else:
                        var92 = 0.004385968
                else:
                    if input[1] < 5.2162094:
                        var92 = 0.010625758
                    else:
                        var92 = 0.00031630966
    if input[35] < 19.148708:
        if input[13] < 0.39241052:
            if input[10] < 0.24074075:
                if input[11] < 0.21397485:
                    if input[22] < 6.2262416:
                        var93 = 0.0020608534
                    else:
                        var93 = 0.00054486
                else:
                    if input[19] < 310.96075:
                        var93 = 0.0007771283
                    else:
                        var93 = -0.0026839913
            else:
                if input[1] < 10.076003:
                    if input[6] < 115.0:
                        var93 = -0.00057461485
                    else:
                        var93 = 0.0007819915
                else:
                    if input[26] < 14.312945:
                        var93 = -0.019582622
                    else:
                        var93 = -0.0016610635
        else:
            if input[35] < 18.340254:
                if input[7] < 1212.0:
                    if input[6] < 2197.0:
                        var93 = 0.00006328298
                    else:
                        var93 = -0.012822099
                else:
                    if input[15] < 29.0:
                        var93 = -0.024072155
                    else:
                        var93 = 0.0025836516
            else:
                if input[0] < 8511.0:
                    if input[35] < 18.604809:
                        var93 = -0.004916722
                    else:
                        var93 = -0.04458287
                else:
                    if input[3] < 5458.909:
                        var93 = 0.01913565
                    else:
                        var93 = 0.0049981317
    else:
        if input[10] < 0.10353011:
            if input[1] < 7.476715:
                if input[26] < 31.340298:
                    if input[2] < 62.0:
                        var93 = -0.010960796
                    else:
                        var93 = 0.013892921
                else:
                    if input[11] < 0.22048691:
                        var93 = -0.022275837
                    else:
                        var93 = 0.010694347
            else:
                if input[30] < 10.0:
                    if input[1] < 9.026796:
                        var93 = -0.0052951607
                    else:
                        var93 = 0.019236518
                else:
                    if input[3] < 4896.476:
                        var93 = -0.02224668
                    else:
                        var93 = -0.002633184
        else:
            if input[12] < 0.2680742:
                if input[26] < 6.327245:
                    if input[10] < 0.29183957:
                        var93 = 0.005758644
                    else:
                        var93 = -0.0070948526
                else:
                    if input[24] < 73801.0:
                        var93 = -0.0025045953
                    else:
                        var93 = 0.000051106897
            else:
                if input[11] < 0.25368324:
                    if input[13] < 0.31385282:
                        var93 = -0.00019298475
                    else:
                        var93 = 0.0037617825
                else:
                    if input[11] < 0.25804585:
                        var93 = 0.01689358
                    else:
                        var93 = 0.0041153114
    if input[1] < 2.5747423:
        if input[13] < 0.30590808:
            if input[2] < 4.0:
                if input[35] < 19.44795:
                    if input[4] < 284.0:
                        var94 = -0.0035049233
                    else:
                        var94 = -0.016487509
                else:
                    if input[10] < 0.19215044:
                        var94 = 0.0053660567
                    else:
                        var94 = 0.018941332
            else:
                if input[25] < 0.0024955638:
                    if input[7] < 839.0:
                        var94 = -0.03544649
                    else:
                        var94 = -0.0022114129
                else:
                    if input[5] < 258.0:
                        var94 = -0.01453603
                    else:
                        var94 = 0.0030625141
        else:
            if input[2] < 5.0:
                if input[7] < 1212.0:
                    if input[3] < 81.210526:
                        var94 = 0.002153693
                    else:
                        var94 = -0.0034323551
                else:
                    if input[11] < 0.1838843:
                        var94 = 0.016190996
                    else:
                        var94 = 0.00051208556
            else:
                if input[35] < 17.74646:
                    if input[35] < 17.452911:
                        var94 = 0.0036465065
                    else:
                        var94 = -0.0038143487
                else:
                    if input[35] < 17.804674:
                        var94 = 0.012259276
                    else:
                        var94 = 0.0031985273
    else:
        if input[1] < 3.0252814:
            if input[11] < 0.07709251:
                if input[26] < 10.362872:
                    if input[22] < 6.514544:
                        var94 = -0.010925803
                    else:
                        var94 = 0.006964651
                else:
                    if input[10] < 0.28774422:
                        var94 = -0.017235935
                    else:
                        var94 = -0.063737914
            else:
                if input[13] < 0.41384995:
                    if input[4] < 5438.0:
                        var94 = -0.0010543084
                    else:
                        var94 = 0.002683684
                else:
                    if input[24] < 22290.0:
                        var94 = 0.0005824234
                    else:
                        var94 = -0.011815329
        else:
            if input[3] < 192.1:
                if input[5] < 256.0:
                    if input[29] < 233.0:
                        var94 = 0.0020851865
                    else:
                        var94 = -0.02236184
                else:
                    if input[17] < 1909.0:
                        var94 = 0.016775358
                    else:
                        var94 = 0.0063869744
            else:
                if input[15] < 28.0:
                    if input[13] < 0.46285716:
                        var94 = 0.000033460576
                    else:
                        var94 = -0.008003747
                else:
                    if input[20] < 14.625984:
                        var94 = 0.0022955684
                    else:
                        var94 = 0.0004738663
    if input[15] < 43.0:
        if input[12] < 0.09598741:
            if input[15] < 20.0:
                if input[8] < 143.0:
                    if input[10] < 0.305761:
                        var95 = -0.0113972295
                    else:
                        var95 = 0.0042786826
                else:
                    if input[2] < 76.0:
                        var95 = -0.041865233
                    else:
                        var95 = 0.018568419
            else:
                if input[22] < 3.9744623:
                    if input[2] < 47.0:
                        var95 = -0.0036793076
                    else:
                        var95 = 0.017395288
                else:
                    if input[22] < 4.3839293:
                        var95 = -0.00864376
                    else:
                        var95 = -0.0008464527
        else:
            if input[11] < 0.08375:
                if input[1] < 5.0221744:
                    if input[22] < 5.385421:
                        var95 = -0.000121512036
                    else:
                        var95 = -0.009788029
                else:
                    if input[24] < 27080.0:
                        var95 = -0.019233389
                    else:
                        var95 = 0.0006967467
            else:
                if input[35] < 17.271885:
                    if input[10] < 0.29183957:
                        var95 = -0.00043913373
                    else:
                        var95 = -0.009642005
                else:
                    if input[11] < 0.20651747:
                        var95 = 0.0006776738
                    else:
                        var95 = 0.00012585582
    else:
        if input[19] < 427.93463:
            if input[35] < 17.109346:
                if input[22] < 7.4495945:
                    var95 = -0.001225991
                else:
                    if input[16] < 36.083652:
                        var95 = -0.019484311
                    else:
                        var95 = -0.005287319
            else:
                if input[35] < 17.352804:
                    if input[16] < 38.44282:
                        var95 = 0.02215287
                    else:
                        var95 = 0.004191346
                else:
                    if input[16] < 38.120872:
                        var95 = -0.0014072711
                    else:
                        var95 = 0.005447756
        else:
            if input[24] < 120109.0:
                if input[4] < 4355.0:
                    if input[22] < 7.5069256:
                        var95 = 0.007646245
                    else:
                        var95 = -0.0027781967
                else:
                    if input[24] < 60908.0:
                        var95 = -0.03775423
                    else:
                        var95 = -0.0025542525
            else:
                if input[4] < 11797.0:
                    if input[22] < 6.202124:
                        var95 = -0.031389166
                    else:
                        var95 = 0.012423456
                else:
                    if input[3] < 6346.6816:
                        var95 = 0.0010210125
                    else:
                        var95 = -0.015012898
    if input[30] < 10.0:
        if input[33] < 169076.0:
            if input[19] < 340.42465:
                if input[5] < 1474.0:
                    if input[11] < 0.102564104:
                        var96 = -0.0052324417
                    else:
                        var96 = -0.00029554075
                else:
                    if input[35] < 18.653639:
                        var96 = -0.015891235
                    else:
                        var96 = 0.002455873
            else:
                if input[15] < 34.0:
                    var96 = -0.008648089
                else:
                    var96 = -0.047545265
        else:
            if input[4] < 10530.0:
                if input[19] < 304.4012:
                    var96 = -0.020852027
                else:
                    if input[0] < 18475.0:
                        var96 = 0.01914517
                    else:
                        var96 = -0.014601058
            else:
                if input[1] < 7.353603:
                    if input[0] < 11593.0:
                        var96 = -0.0073474734
                    else:
                        var96 = -0.024680337
                else:
                    if input[0] < 11593.0:
                        var96 = 0.0064185183
                    else:
                        var96 = 0.00097083574
    else:
        if input[4] < 86.0:
            if input[29] < 87.0:
                if input[5] < 77.0:
                    if input[1] < 2.2915876:
                        var96 = -0.00025887263
                    else:
                        var96 = 0.018203046
                else:
                    if input[29] < 80.0:
                        var96 = -0.012664877
                    else:
                        var96 = 0.00091868144
            else:
                if input[16] < 20.206203:
                    var96 = 0.02637515
                else:
                    if input[16] < 20.416943:
                        var96 = -0.030476633
                    else:
                        var96 = 0.006300745
        else:
            if input[24] < 2467.0:
                if input[3] < 61.473682:
                    if input[20] < 12.012411:
                        var96 = -0.022708524
                    else:
                        var96 = -0.00009959423
                else:
                    if input[11] < 0.24220484:
                        var96 = -0.008266988
                    else:
                        var96 = -0.037466742
            else:
                if input[3] < 81.210526:
                    if input[13] < 0.39587975:
                        var96 = 0.0077713663
                    else:
                        var96 = 0.00016697391
                else:
                    if input[24] < 3235.0:
                        var96 = -0.009282614
                    else:
                        var96 = 0.00035945562
    if input[10] < 0.35:
        if input[5] < 71.0:
            if input[17] < 751.0:
                if input[8] < 206.0:
                    if input[1] < 10.973457:
                        var97 = -0.00033278667
                    else:
                        var97 = -0.008767712
                else:
                    if input[7] < 87.0:
                        var97 = 0.0073820017
                    else:
                        var97 = 0.023127351
            else:
                if input[3] < 4194.2856:
                    if input[3] < 3106.3635:
                        var97 = -0.005469844
                    else:
                        var97 = 0.008603602
                else:
                    if input[7] < 196.0:
                        var97 = -0.016444549
                    else:
                        var97 = 0.011377596
        else:
            if input[15] < 43.0:
                if input[22] < 8.324042:
                    if input[35] < 19.148708:
                        var97 = 0.00041058628
                    else:
                        var97 = -0.00037073615
                else:
                    if input[2] < 32.0:
                        var97 = 0.0057316055
                    else:
                        var97 = -0.010353784
            else:
                if input[10] < 0.13791667:
                    if input[10] < 0.09416445:
                        var97 = 0.006942471
                    else:
                        var97 = -0.005895553
                else:
                    if input[4] < 15068.0:
                        var97 = 0.0031877276
                    else:
                        var97 = -0.010674747
    else:
        if input[20] < 16.546991:
            if input[0] < 2159.0:
                if input[8] < 719.0:
                    if input[7] < 163.0:
                        var97 = -0.0017653358
                    else:
                        var97 = 0.004851406
                else:
                    if input[7] < 322.0:
                        var97 = -0.027998278
                    else:
                        var97 = 0.008860778
            else:
                if input[7] < 413.0:
                    if input[8] < 1057.0:
                        var97 = 0.02296632
                    else:
                        var97 = 0.0007956293
                else:
                    if input[1] < 6.9273744:
                        var97 = 0.009265915
                    else:
                        var97 = -0.007132642
        else:
            if input[20] < 16.996424:
                if input[4] < 7850.0:
                    if input[1] < 6.4393086:
                        var97 = -0.011003942
                    else:
                        var97 = 0.0051864446
                else:
                    if input[7] < 131.0:
                        var97 = -0.007129211
                    else:
                        var97 = -0.05285343
            else:
                if input[4] < 14003.0:
                    if input[13] < 0.3180723:
                        var97 = -0.006915256
                    else:
                        var97 = -0.0003610409
                else:
                    var97 = -0.035531256
    if input[30] < 18.0:
        if input[22] < 6.178954:
            if input[15] < 28.0:
                if input[16] < 26.305569:
                    if input[22] < 5.404372:
                        var98 = 0.00043240676
                    else:
                        var98 = -0.0016346779
                else:
                    if input[13] < 0.44552845:
                        var98 = -0.0011658234
                    else:
                        var98 = -0.014562815
            else:
                if input[16] < 31.591837:
                    if input[12] < 0.32611465:
                        var98 = 0.0009368904
                    else:
                        var98 = 0.005686136
                else:
                    if input[10] < 0.3643846:
                        var98 = -0.00000049545014
                    else:
                        var98 = -0.010946437
        else:
            if input[22] < 6.665479:
                if input[11] < 0.3506606:
                    if input[26] < 4.6979604:
                        var98 = 0.0028438836
                    else:
                        var98 = -0.001560538
                else:
                    if input[3] < 4690.636:
                        var98 = -0.0067169974
                    else:
                        var98 = -0.038527098
            else:
                if input[5] < 95.0:
                    if input[20] < 16.606812:
                        var98 = -0.014233305
                    else:
                        var98 = 0.0069109784
                else:
                    if input[11] < 0.36167213:
                        var98 = 0.0005990855
                    else:
                        var98 = 0.012638933
    else:
        if input[15] < 27.0:
            if input[2] < 96.0:
                if input[19] < 124.3672:
                    if input[16] < 25.600283:
                        var98 = 0.0023184065
                    else:
                        var98 = 0.0077070394
                else:
                    if input[5] < 227.0:
                        var98 = 0.0024854154
                    else:
                        var98 = -0.024843043
            else:
                if input[6] < 71.0:
                    var98 = -0.041268643
                else:
                    if input[24] < 98016.0:
                        var98 = 0.006853433
                    else:
                        var98 = -0.01111571
        else:
            if input[1] < 6.83554:
                if input[1] < 6.12425:
                    if input[1] < 6.0992475:
                        var98 = 0.00066925655
                    else:
                        var98 = -0.009509376
                else:
                    if input[11] < 0.16968215:
                        var98 = -0.00069369737
                    else:
                        var98 = 0.0041944445
            else:
                if input[4] < 3781.0:
                    if input[3] < 546.9:
                        var98 = -0.03391407
                    else:
                        var98 = 0.002732897
                else:
                    if input[24] < 64572.0:
                        var98 = -0.0029568253
                    else:
                        var98 = 0.00008464236
    if input[10] < 0.10747664:
        if input[26] < 170.85095:
            if input[2] < 18.0:
                if input[4] < 2565.0:
                    if input[11] < 0.33568075:
                        var99 = -0.0032155798
                    else:
                        var99 = -0.018521024
                else:
                    if input[7] < 1020.0:
                        var99 = -0.037828922
                    else:
                        var99 = -0.0019697528
            else:
                if input[1] < 7.1251564:
                    if input[13] < 0.45728898:
                        var99 = 0.0015409611
                    else:
                        var99 = 0.01686742
                else:
                    if input[1] < 10.697594:
                        var99 = -0.0042793937
                    else:
                        var99 = 0.006349602
        else:
            if input[5] < 61.0:
                if input[24] < 105175.0:
                    if input[3] < 4004.8096:
                        var99 = -0.0047646775
                    else:
                        var99 = -0.03416821
                else:
                    if input[7] < 127.0:
                        var99 = -0.0024216403
                    else:
                        var99 = 0.01431379
            else:
                if input[1] < 4.9770117:
                    var99 = -0.008309204
                else:
                    var99 = -0.05037273
    else:
        if input[2] < 10.0:
            if input[24] < 16390.0:
                if input[3] < 455.15:
                    if input[10] < 0.31768888:
                        var99 = 0.0012645635
                    else:
                        var99 = -0.0047126873
                else:
                    if input[4] < 898.0:
                        var99 = -0.03393248
                    else:
                        var99 = -0.0072795227
            else:
                if input[35] < 17.159575:
                    if input[10] < 0.24722503:
                        var99 = 0.0011855616
                    else:
                        var99 = -0.03477326
                else:
                    if input[13] < 0.36757424:
                        var99 = 0.001829722
                    else:
                        var99 = 0.00792297
        else:
            if input[15] < 20.0:
                if input[25] < 0.04212845:
                    var99 = -0.042395484
                else:
                    if input[24] < 152717.0:
                        var99 = -0.0014178213
                    else:
                        var99 = 0.014525281
            else:
                if input[11] < 0.08375:
                    if input[1] < 3.550686:
                        var99 = -0.017137898
                    else:
                        var99 = -0.0011412501
                else:
                    if input[12] < 0.28401726:
                        var99 = 0.00018698332
                    else:
                        var99 = 0.0012327794
    if input[13] < 0.46285716:
        if input[30] < 10.0:
            if input[35] < 20.16387:
                if input[3] < 6042.5454:
                    if input[2] < 97.0:
                        var100 = -0.0005585203
                    else:
                        var100 = 0.0053752544
                else:
                    if input[16] < 18.382183:
                        var100 = 0.011587106
                    else:
                        var100 = -0.0071723456
            else:
                if input[1] < 3.8153753:
                    var100 = 0.0032752554
                else:
                    if input[1] < 7.1251564:
                        var100 = -0.012794304
                    else:
                        var100 = -0.033190854
        else:
            if input[15] < 45.0:
                if input[13] < 0.2934363:
                    if input[4] < 13240.0:
                        var100 = -0.0015374554
                    else:
                        var100 = 0.010824945
                else:
                    if input[10] < 0.15306123:
                        var100 = -0.0003509959
                    else:
                        var100 = 0.00039656094
            else:
                if input[19] < 387.07837:
                    if input[20] < 21.302843:
                        var100 = -0.008509403
                    else:
                        var100 = 0.0077974196
                else:
                    if input[35] < 18.259357:
                        var100 = -0.0022068447
                    else:
                        var100 = 0.003994007
    else:
        if input[29] < 122.0:
            if input[22] < 5.648443:
                if input[2] < 86.0:
                    if input[8] < 395.0:
                        var100 = -0.0041335053
                    else:
                        var100 = 0.013362937
                else:
                    if input[35] < 16.951084:
                        var100 = -0.0076682414
                    else:
                        var100 = -0.03191427
            else:
                if input[10] < 0.17613636:
                    if input[22] < 6.6296387:
                        var100 = -0.032067284
                    else:
                        var100 = -0.011230908
                else:
                    var100 = 0.00067901716
        else:
            if input[11] < 0.27228683:
                if input[24] < 117219.0:
                    if input[24] < 94796.0:
                        var100 = -0.0022370631
                    else:
                        var100 = 0.0065777185
                else:
                    if input[24] < 127044.0:
                        var100 = -0.025028495
                    else:
                        var100 = -0.002339313
            else:
                if input[10] < 0.13217391:
                    if input[2] < 72.0:
                        var100 = 0.028194537
                    else:
                        var100 = 0.012764891
                else:
                    var100 = -0.009176031
    return nan + (var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99 + var100)
