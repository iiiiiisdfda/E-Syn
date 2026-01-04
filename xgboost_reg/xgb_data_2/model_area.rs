fn score(input: Vec<f64>) -> f64 {
    let var0: f64;
    if input[7] < 128.0_f64 {
        if input[7] < 58.0_f64 {
            var0 = 0.09713098_f64;
        } else {
            var0 = 0.097767256_f64;
        }
    } else {
        if input[7] < 299.0_f64 {
            var0 = 0.09813459_f64;
        } else {
            var0 = 0.09840027_f64;
        }
    }
    let var1: f64;
    if input[7] < 129.0_f64 {
        if input[7] < 64.0_f64 {
            var1 = 0.09693212_f64;
        } else {
            var1 = 0.09756402_f64;
        }
    } else {
        if input[7] < 304.0_f64 {
            var1 = 0.09794647_f64;
        } else {
            var1 = 0.09823713_f64;
        }
    }
    let var2: f64;
    if input[7] < 151.0_f64 {
        if input[7] < 72.0_f64 {
            if input[7] < 41.0_f64 {
                var2 = 0.09597906_f64;
            } else {
                var2 = 0.09686624_f64;
            }
        } else {
            var2 = 0.09741046_f64;
        }
    } else {
        if input[7] < 304.0_f64 {
            var2 = 0.0977669_f64;
        } else {
            var2 = 0.09805516_f64;
        }
    }
    let var3: f64;
    if input[7] < 127.0_f64 {
        if input[7] < 63.0_f64 {
            var3 = 0.096259795_f64;
        } else {
            var3 = 0.09702812_f64;
        }
    } else {
        if input[7] < 299.0_f64 {
            var3 = 0.09749507_f64;
        } else {
            var3 = 0.097852044_f64;
        }
    }
    let var4: f64;
    if input[7] < 125.0_f64 {
        if input[7] < 58.0_f64 {
            var4 = 0.09577549_f64;
        } else {
            var4 = 0.09669065_f64;
        }
    } else {
        if input[7] < 299.0_f64 {
            var4 = 0.09723521_f64;
        } else {
            if input[30] < 15.0_f64 {
                var4 = 0.09748665_f64;
            } else {
                var4 = 0.097734824_f64;
            }
        }
    }
    let var5: f64;
    if input[7] < 128.0_f64 {
        if input[7] < 63.0_f64 {
            if input[7] < 38.0_f64 {
                var5 = 0.09445398_f64;
            } else {
                var5 = 0.095662594_f64;
            }
        } else {
            var5 = 0.09639513_f64;
        }
    } else {
        if input[7] < 307.0_f64 {
            if input[30] < 14.0_f64 {
                var5 = 0.09680157_f64;
            } else {
                var5 = 0.097086795_f64;
            }
        } else {
            var5 = 0.09739432_f64;
        }
    }
    let var6: f64;
    if input[7] < 128.0_f64 {
        if input[7] < 63.0_f64 {
            if input[7] < 38.0_f64 {
                var6 = 0.093904674_f64;
            } else {
                var6 = 0.09522719_f64;
            }
        } else {
            var6 = 0.09603033_f64;
        }
    } else {
        if input[7] < 307.0_f64 {
            if input[30] < 13.0_f64 {
                var6 = 0.09643957_f64;
            } else {
                var6 = 0.09676599_f64;
            }
        } else {
            if input[30] < 15.0_f64 {
                var6 = 0.096954204_f64;
            } else {
                var6 = 0.0972518_f64;
            }
        }
    }
    let var7: f64;
    if input[7] < 153.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 41.0_f64 {
                var7 = 0.093521334_f64;
            } else {
                var7 = 0.09491155_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                var7 = 0.09552566_f64;
            } else {
                var7 = 0.09598266_f64;
            }
        }
    } else {
        if input[7] < 329.0_f64 {
            if input[30] < 14.0_f64 {
                var7 = 0.09619352_f64;
            } else {
                var7 = 0.09653174_f64;
            }
        } else {
            if input[30] < 15.0_f64 {
                var7 = 0.09666487_f64;
            } else {
                var7 = 0.0969868_f64;
            }
        }
    }
    let var8: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 41.0_f64 {
                var8 = 0.09288628_f64;
            } else {
                var8 = 0.09440495_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                var8 = 0.09507717_f64;
            } else {
                var8 = 0.09558251_f64;
            }
        }
    } else {
        if input[7] < 319.0_f64 {
            if input[30] < 14.0_f64 {
                var8 = 0.095804185_f64;
            } else {
                var8 = 0.096178204_f64;
            }
        } else {
            if input[30] < 14.0_f64 {
                var8 = 0.09627866_f64;
            } else {
                var8 = 0.09664569_f64;
            }
        }
    }
    let var9: f64;
    if input[7] < 153.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 41.0_f64 {
                var9 = 0.09219393_f64;
            } else {
                var9 = 0.09385103_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                var9 = 0.09458616_f64;
            } else {
                var9 = 0.09513443_f64;
            }
        }
    } else {
        if input[7] < 329.0_f64 {
            if input[30] < 13.0_f64 {
                var9 = 0.09533749_f64;
            } else {
                var9 = 0.095763676_f64;
            }
        } else {
            if input[30] < 15.0_f64 {
                var9 = 0.0959548_f64;
            } else {
                var9 = 0.09634303_f64;
            }
        }
    }
    let var10: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 41.0_f64 {
                var10 = 0.09144015_f64;
            } else {
                var10 = 0.093246005_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                var10 = 0.09404909_f64;
            } else {
                var10 = 0.094654225_f64;
            }
        }
    } else {
        if input[7] < 316.0_f64 {
            if input[30] < 14.0_f64 {
                var10 = 0.09492091_f64;
            } else {
                var10 = 0.09536438_f64;
            }
        } else {
            if input[30] < 15.0_f64 {
                var10 = 0.095533244_f64;
            } else {
                var10 = 0.095961265_f64;
            }
        }
    }
    let var11: f64;
    if input[7] < 154.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 41.0_f64 {
                var11 = 0.09062066_f64;
            } else {
                var11 = 0.09258595_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                var11 = 0.09346226_f64;
            } else {
                var11 = 0.094120994_f64;
            }
        }
    } else {
        if input[7] < 329.0_f64 {
            if input[30] < 13.0_f64 {
                var11 = 0.094363995_f64;
            } else {
                var11 = 0.09487535_f64;
            }
        } else {
            if input[30] < 15.0_f64 {
                var11 = 0.09510106_f64;
            } else {
                var11 = 0.095567614_f64;
            }
        }
    }
    let var12: f64;
    if input[7] < 154.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 41.0_f64 {
                var12 = 0.08973115_f64;
            } else {
                var12 = 0.091866754_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                var12 = 0.09282177_f64;
            } else {
                var12 = 0.09354078_f64;
            }
        }
    } else {
        if input[7] < 329.0_f64 {
            if input[30] < 14.0_f64 {
                var12 = 0.09387248_f64;
            } else {
                var12 = 0.094406_f64;
            }
        } else {
            if input[30] < 15.0_f64 {
                var12 = 0.09461229_f64;
            } else {
                var12 = 0.09512313_f64;
            }
        }
    }
    let var13: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 41.0_f64 {
                var13 = 0.08876728_f64;
            } else {
                var13 = 0.09108421_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                var13 = 0.09212359_f64;
            } else {
                var13 = 0.09291031_f64;
            }
        }
    } else {
        if input[7] < 347.0_f64 {
            if input[30] < 13.0_f64 {
                var13 = 0.093221076_f64;
            } else {
                var13 = 0.09383624_f64;
            }
        } else {
            if input[30] < 15.0_f64 {
                var13 = 0.09409721_f64;
            } else {
                var13 = 0.094655134_f64;
            }
        }
    }
    let var14: f64;
    if input[7] < 154.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 38.0_f64 {
                var14 = 0.08731466_f64;
            } else {
                var14 = 0.09016784_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                var14 = 0.09136353_f64;
            } else {
                if input[30] < 14.0_f64 {
                    var14 = 0.091836415_f64;
                } else {
                    var14 = 0.0925714_f64;
                }
            }
        }
    } else {
        if input[7] < 347.0_f64 {
            if input[30] < 13.0_f64 {
                var14 = 0.09255646_f64;
            } else {
                var14 = 0.09322503_f64;
            }
        } else {
            if input[30] < 14.0_f64 {
                var14 = 0.09344161_f64;
            } else {
                if input[12] < 0.19248678_f64 {
                    var14 = 0.0936879_f64;
                } else {
                    var14 = 0.094253324_f64;
                }
            }
        }
    }
    let var15: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 41.0_f64 {
                var15 = 0.086595014_f64;
            } else {
                var15 = 0.08931257_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                if input[30] < 13.0_f64 {
                    var15 = 0.09005432_f64;
                } else {
                    var15 = 0.09094622_f64;
                }
            } else {
                if input[30] < 14.0_f64 {
                    var15 = 0.091063775_f64;
                } else {
                    var15 = 0.091845326_f64;
                }
            }
        }
    } else {
        if input[7] < 329.0_f64 {
            if input[30] < 14.0_f64 {
                if input[12] < 0.19248678_f64 {
                    var15 = 0.09142255_f64;
                } else {
                    var15 = 0.09218912_f64;
                }
            } else {
                var15 = 0.09259442_f64;
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.20056497_f64 {
                    var15 = 0.0923511_f64;
                } else {
                    var15 = 0.09311006_f64;
                }
            } else {
                if input[12] < 0.18503119_f64 {
                    var15 = 0.09307835_f64;
                } else {
                    var15 = 0.09368526_f64;
                }
            }
        }
    }
    let var16: f64;
    if input[7] < 154.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 38.0_f64 {
                var16 = 0.084905885_f64;
            } else {
                var16 = 0.088236526_f64;
            }
        } else {
            if input[7] < 106.0_f64 {
                if input[30] < 13.0_f64 {
                    var16 = 0.089117154_f64;
                } else {
                    var16 = 0.09008425_f64;
                }
            } else {
                if input[30] < 14.0_f64 {
                    var16 = 0.090198085_f64;
                } else {
                    var16 = 0.09106703_f64;
                }
            }
        }
    } else {
        if input[7] < 329.0_f64 {
            if input[30] < 14.0_f64 {
                if input[12] < 0.19414414_f64 {
                    var16 = 0.090613715_f64;
                } else {
                    var16 = 0.09144043_f64;
                }
            } else {
                var16 = 0.091868535_f64;
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.20056497_f64 {
                    var16 = 0.091611095_f64;
                } else {
                    var16 = 0.09243774_f64;
                }
            } else {
                if input[12] < 0.18503119_f64 {
                    var16 = 0.09240318_f64;
                } else {
                    var16 = 0.093065076_f64;
                }
            }
        }
    }
    let var17: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 73.0_f64 {
            if input[7] < 41.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var17 = 0.081581846_f64;
                    } else {
                        var17 = 0.04284333_f64;
                    }
                } else {
                    var17 = 0.08475366_f64;
                }
            } else {
                var17 = 0.087302715_f64;
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[7] < 104.0_f64 {
                    var17 = 0.08820168_f64;
                } else {
                    var17 = 0.089269295_f64;
                }
            } else {
                if input[7] < 106.0_f64 {
                    var17 = 0.089278854_f64;
                } else {
                    var17 = 0.09020852_f64;
                }
            }
        }
    } else {
        if input[7] < 326.0_f64 {
            if input[30] < 14.0_f64 {
                if input[12] < 0.19414414_f64 {
                    var17 = 0.089718066_f64;
                } else {
                    var17 = 0.09062233_f64;
                }
            } else {
                if input[11] < 0.24438202_f64 {
                    var17 = 0.09127034_f64;
                } else {
                    var17 = 0.090484895_f64;
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.20056497_f64 {
                    var17 = 0.09079712_f64;
                } else {
                    var17 = 0.09169819_f64;
                }
            } else {
                if input[7] < 765.0_f64 {
                    var17 = 0.09195196_f64;
                } else {
                    var17 = 0.09262078_f64;
                }
            }
        }
    }
    let var18: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 73.0_f64 {
            if input[7] < 41.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var18 = 0.080018364_f64;
                    } else {
                        var18 = 0.040834766_f64;
                    }
                } else {
                    var18 = 0.08340562_f64;
                }
            } else {
                var18 = 0.08614444_f64;
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[7] < 104.0_f64 {
                    var18 = 0.08711385_f64;
                } else {
                    var18 = 0.08826735_f64;
                }
            } else {
                if input[7] < 106.0_f64 {
                    var18 = 0.08827773_f64;
                } else {
                    var18 = 0.08928422_f64;
                }
            }
        }
    } else {
        if input[7] < 329.0_f64 {
            if input[30] < 14.0_f64 {
                if input[12] < 0.19414414_f64 {
                    var18 = 0.08875548_f64;
                } else {
                    var18 = 0.08973435_f64;
                }
            } else {
                if input[11] < 0.24438202_f64 {
                    var18 = 0.09044359_f64;
                } else {
                    var18 = 0.08959318_f64;
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.20056497_f64 {
                    var18 = 0.089932516_f64;
                } else {
                    var18 = 0.09090884_f64;
                }
            } else {
                if input[7] < 765.0_f64 {
                    var18 = 0.09117834_f64;
                } else {
                    var18 = 0.09190469_f64;
                }
            }
        }
    }
    let var19: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 38.0_f64 {
                var19 = 0.08059993_f64;
            } else {
                if input[7] < 50.0_f64 {
                    var19 = 0.08351936_f64;
                } else {
                    var19 = 0.08512059_f64;
                }
            }
        } else {
            if input[7] < 106.0_f64 {
                if input[30] < 13.0_f64 {
                    var19 = 0.08582275_f64;
                } else {
                    var19 = 0.087048784_f64;
                }
            } else {
                if input[30] < 14.0_f64 {
                    var19 = 0.0872068_f64;
                } else {
                    var19 = 0.0882835_f64;
                }
            }
        }
    } else {
        if input[7] < 347.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.19354838_f64 {
                    var19 = 0.08757667_f64;
                } else {
                    var19 = 0.08870482_f64;
                }
            } else {
                if input[11] < 0.24438202_f64 {
                    if input[7] < 205.0_f64 {
                        var19 = 0.088968866_f64;
                    } else {
                        var19 = 0.089741185_f64;
                    }
                } else {
                    var19 = 0.088602096_f64;
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.20295984_f64 {
                    var19 = 0.088922195_f64;
                } else {
                    var19 = 0.08995643_f64;
                }
            } else {
                if input[12] < 0.19248678_f64 {
                    var19 = 0.08997822_f64;
                } else {
                    var19 = 0.090856954_f64;
                }
            }
        }
    }
    let var20: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 73.0_f64 {
            if input[7] < 41.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var20 = 0.07654231_f64;
                    } else {
                        var20 = 0.03485447_f64;
                    }
                } else {
                    var20 = 0.08043049_f64;
                }
            } else {
                if input[30] < 13.0_f64 {
                    var20 = 0.08296981_f64;
                } else {
                    var20 = 0.08433629_f64;
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[7] < 104.0_f64 {
                    var20 = 0.08467796_f64;
                } else {
                    var20 = 0.08601768_f64;
                }
            } else {
                if input[7] < 110.0_f64 {
                    var20 = 0.08610649_f64;
                } else {
                    var20 = 0.08724665_f64;
                }
            }
        }
    } else {
        if input[7] < 347.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.19354838_f64 {
                    var20 = 0.0864397_f64;
                } else {
                    var20 = 0.087657146_f64;
                }
            } else {
                if input[11] < 0.24438202_f64 {
                    if input[7] < 205.0_f64 {
                        var20 = 0.08794251_f64;
                    } else {
                        var20 = 0.088778_f64;
                    }
                } else {
                    var20 = 0.08754619_f64;
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.20295984_f64 {
                    var20 = 0.08789208_f64;
                } else {
                    var20 = 0.089011095_f64;
                }
            } else {
                if input[12] < 0.19248678_f64 {
                    var20 = 0.0890347_f64;
                } else {
                    var20 = 0.08998735_f64;
                }
            }
        }
    }
    let var21: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 73.0_f64 {
            if input[7] < 41.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var21 = 0.07467948_f64;
                    } else {
                        var21 = 0.033059414_f64;
                    }
                } else {
                    var21 = 0.07879223_f64;
                }
            } else {
                if input[30] < 13.0_f64 {
                    var21 = 0.08149671_f64;
                } else {
                    var21 = 0.082958184_f64;
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[7] < 104.0_f64 {
                    var21 = 0.0833241_f64;
                } else {
                    var21 = 0.08476177_f64;
                }
            } else {
                if input[7] < 106.0_f64 {
                    var21 = 0.08477556_f64;
                } else {
                    var21 = 0.086036645_f64;
                }
            }
        }
    } else {
        if input[7] < 347.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.19354838_f64 {
                    if input[5] < 1883.0_f64 {
                        var21 = 0.08522091_f64;
                    } else {
                        var21 = 0.035298433_f64;
                    }
                } else {
                    var21 = 0.08652642_f64;
                }
            } else {
                if input[11] < 0.25714287_f64 {
                    if input[7] < 205.0_f64 {
                        var21 = 0.08680483_f64;
                    } else {
                        var21 = 0.08769424_f64;
                    }
                } else {
                    var21 = 0.086243235_f64;
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.20295984_f64 {
                    var21 = 0.0867798_f64;
                } else {
                    var21 = 0.08798815_f64;
                }
            } else {
                if input[12] < 0.19248678_f64 {
                    var21 = 0.088013664_f64;
                } else {
                    if input[7] < 819.0_f64 {
                        var21 = 0.08874999_f64;
                    } else {
                        var21 = 0.0895443_f64;
                    }
                }
            }
        }
    }
    let var22: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 38.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var22 = 0.072719745_f64;
                    } else {
                        var22 = 0.031324483_f64;
                    }
                } else {
                    var22 = 0.07652222_f64;
                }
            } else {
                if input[7] < 50.0_f64 {
                    if input[10] < 0.11857708_f64 {
                        var22 = 0.02895433_f64;
                    } else {
                        var22 = 0.07890651_f64;
                    }
                } else {
                    var22 = 0.08087876_f64;
                }
            }
        } else {
            if input[7] < 106.0_f64 {
                if input[30] < 13.0_f64 {
                    var22 = 0.08172701_f64;
                } else {
                    var22 = 0.083248965_f64;
                }
            } else {
                if input[30] < 14.0_f64 {
                    var22 = 0.08344172_f64;
                } else {
                    var22 = 0.084782146_f64;
                }
            }
        }
    } else {
        if input[7] < 329.0_f64 {
            if input[30] < 14.0_f64 {
                if input[12] < 0.19414414_f64 {
                    if input[5] < 1883.0_f64 {
                        var22 = 0.08406196_f64;
                    } else {
                        var22 = 0.0337439_f64;
                    }
                } else {
                    var22 = 0.085387625_f64;
                }
            } else {
                if input[11] < 0.24438202_f64 {
                    var22 = 0.08635973_f64;
                } else {
                    var22 = 0.08519885_f64;
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.21534973_f64 {
                    var22 = 0.08581249_f64;
                } else {
                    if input[15] < 30.0_f64 {
                        var22 = 0.08638429_f64;
                    } else {
                        var22 = 0.087554656_f64;
                    }
                }
            } else {
                if input[7] < 765.0_f64 {
                    if input[12] < 0.18503119_f64 {
                        var22 = 0.08662278_f64;
                    } else {
                        var22 = 0.087673336_f64;
                    }
                } else {
                    var22 = 0.088380545_f64;
                }
            }
        }
    }
    let var23: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 73.0_f64 {
            if input[7] < 44.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var23 = 0.070666075_f64;
                    } else {
                        var23 = 0.029651647_f64;
                    }
                } else {
                    var23 = 0.075637095_f64;
                }
            } else {
                if input[30] < 13.0_f64 {
                    var23 = 0.07838773_f64;
                } else {
                    var23 = 0.08000518_f64;
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[7] < 104.0_f64 {
                    var23 = 0.08032661_f64;
                } else {
                    if input[12] < 0.15955351_f64 {
                        var23 = 0.08085343_f64;
                    } else {
                        var23 = 0.08233307_f64;
                    }
                }
            } else {
                if input[7] < 110.0_f64 {
                    var23 = 0.082080774_f64;
                } else {
                    var23 = 0.083492_f64;
                }
            }
        }
    } else {
        if input[7] < 347.0_f64 {
            if input[30] < 15.0_f64 {
                if input[12] < 0.20240137_f64 {
                    if input[11] < 0.34256172_f64 {
                        var23 = 0.083078094_f64;
                    } else {
                        var23 = 0.07930241_f64;
                    }
                } else {
                    var23 = 0.08432223_f64;
                }
            } else {
                if input[12] < 0.1473772_f64 {
                    var23 = 0.083783604_f64;
                } else {
                    var23 = 0.08524219_f64;
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.21595487_f64 {
                    var23 = 0.08459346_f64;
                } else {
                    if input[15] < 30.0_f64 {
                        var23 = 0.085166015_f64;
                    } else {
                        var23 = 0.086430125_f64;
                    }
                }
            } else {
                if input[12] < 0.18503119_f64 {
                    var23 = 0.08575267_f64;
                } else {
                    if input[7] < 819.0_f64 {
                        var23 = 0.08661805_f64;
                    } else {
                        var23 = 0.08756732_f64;
                    }
                }
            }
        }
    }
    let var24: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 79.0_f64 {
            if input[7] < 44.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var24 = 0.06852271_f64;
                    } else {
                        var24 = 0.02804229_f64;
                    }
                } else {
                    var24 = 0.073723674_f64;
                }
            } else {
                if input[30] < 12.0_f64 {
                    var24 = 0.0766764_f64;
                } else {
                    var24 = 0.07843652_f64;
                }
            }
        } else {
            if input[30] < 13.0_f64 {
                if input[7] < 106.0_f64 {
                    if input[6] < 470.0_f64 {
                        var24 = 0.078726724_f64;
                    } else {
                        var24 = 0.04475728_f64;
                    }
                } else {
                    if input[12] < 0.15883978_f64 {
                        var24 = 0.07897915_f64;
                    } else {
                        var24 = 0.08070684_f64;
                    }
                }
            } else {
                if input[7] < 110.0_f64 {
                    var24 = 0.080570705_f64;
                } else {
                    var24 = 0.08193248_f64;
                }
            }
        }
    } else {
        if input[7] < 347.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.19354838_f64 {
                    if input[5] < 1883.0_f64 {
                        var24 = 0.08097955_f64;
                    } else {
                        var24 = 0.028469948_f64;
                    }
                } else {
                    if input[6] < 570.0_f64 {
                        var24 = 0.08259719_f64;
                    } else {
                        var24 = 0.03234353_f64;
                    }
                }
            } else {
                if input[12] < 0.1473772_f64 {
                    var24 = 0.08218008_f64;
                } else {
                    if input[7] < 205.0_f64 {
                        var24 = 0.083007485_f64;
                    } else {
                        var24 = 0.08399435_f64;
                    }
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.20295984_f64 {
                    var24 = 0.08290289_f64;
                } else {
                    if input[15] < 31.0_f64 {
                        var24 = 0.08381956_f64;
                    } else {
                        var24 = 0.085036166_f64;
                    }
                }
            } else {
                if input[12] < 0.19248678_f64 {
                    var24 = 0.084442146_f64;
                } else {
                    if input[7] < 819.0_f64 {
                        var24 = 0.08536812_f64;
                    } else {
                        var24 = 0.08636927_f64;
                    }
                }
            }
        }
    }
    let var25: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 38.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var25 = 0.06629523_f64;
                    } else {
                        var25 = 0.026497269_f64;
                    }
                } else {
                    var25 = 0.0705778_f64;
                }
            } else {
                if input[7] < 50.0_f64 {
                    if input[10] < 0.11857708_f64 {
                        var25 = 0.020157108_f64;
                    } else {
                        var25 = 0.0733918_f64;
                    }
                } else {
                    if input[30] < 11.0_f64 {
                        var25 = 0.07431471_f64;
                    } else {
                        var25 = 0.076402925_f64;
                    }
                }
            }
        } else {
            if input[7] < 106.0_f64 {
                if input[30] < 13.0_f64 {
                    if input[6] < 470.0_f64 {
                        var25 = 0.07677417_f64;
                    } else {
                        var25 = 0.042711474_f64;
                    }
                } else {
                    if input[12] < 0.13910761_f64 {
                        var25 = 0.07708009_f64;
                    } else {
                        var25 = 0.07914309_f64;
                    }
                }
            } else {
                if input[30] < 14.0_f64 {
                    if input[12] < 0.16666667_f64 {
                        var25 = 0.07771206_f64;
                    } else {
                        var25 = 0.0792822_f64;
                    }
                } else {
                    var25 = 0.08046015_f64;
                }
            }
        }
    } else {
        if input[7] < 319.0_f64 {
            if input[30] < 14.0_f64 {
                if input[12] < 0.15883978_f64 {
                    if input[5] < 107.0_f64 {
                        var25 = 0.021031925_f64;
                    } else {
                        var25 = 0.07879865_f64;
                    }
                } else {
                    if input[11] < 0.27228683_f64 {
                        var25 = 0.08103945_f64;
                    } else {
                        var25 = 0.07886418_f64;
                    }
                }
            } else {
                if input[12] < 0.14899713_f64 {
                    var25 = 0.08066841_f64;
                } else {
                    if input[11] < 0.25531915_f64 {
                        var25 = 0.08249371_f64;
                    } else {
                        var25 = 0.08111768_f64;
                    }
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.20056497_f64 {
                    if input[5] < 80.0_f64 {
                        var25 = 0.030888034_f64;
                    } else {
                        var25 = 0.08150564_f64;
                    }
                } else {
                    if input[15] < 31.0_f64 {
                        var25 = 0.08248057_f64;
                    } else {
                        var25 = 0.08380551_f64;
                    }
                }
            } else {
                if input[7] < 765.0_f64 {
                    if input[12] < 0.18503119_f64 {
                        var25 = 0.08271096_f64;
                    } else {
                        var25 = 0.08399036_f64;
                    }
                } else {
                    var25 = 0.08491073_f64;
                }
            }
        }
    }
    let var26: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 79.0_f64 {
            if input[7] < 46.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var26 = 0.063990615_f64;
                    } else {
                        var26 = 0.025016908_f64;
                    }
                } else {
                    if input[10] < 0.11857708_f64 {
                        var26 = 0.019188274_f64;
                    } else {
                        var26 = 0.06993963_f64;
                    }
                }
            } else {
                if input[30] < 16.0_f64 {
                    if input[7] < 59.0_f64 {
                        var26 = 0.07232796_f64;
                    } else {
                        var26 = 0.07415713_f64;
                    }
                } else {
                    var26 = 0.075941056_f64;
                }
            }
        } else {
            if input[30] < 13.0_f64 {
                if input[7] < 106.0_f64 {
                    if input[10] < 0.3962926_f64 {
                        var26 = 0.07514909_f64;
                    } else {
                        var26 = 0.03814724_f64;
                    }
                } else {
                    if input[12] < 0.14356436_f64 {
                        var26 = 0.07496902_f64;
                    } else {
                        var26 = 0.07726167_f64;
                    }
                }
            } else {
                if input[7] < 110.0_f64 {
                    if input[12] < 0.1418919_f64 {
                        var26 = 0.07567753_f64;
                    } else {
                        var26 = 0.07774923_f64;
                    }
                } else {
                    var26 = 0.07875213_f64;
                }
            }
        }
    } else {
        if input[7] < 347.0_f64 {
            if input[30] < 15.0_f64 {
                if input[12] < 0.20240137_f64 {
                    if input[11] < 0.29132232_f64 {
                        var26 = 0.078526_f64;
                    } else {
                        var26 = 0.07628469_f64;
                    }
                } else {
                    var26 = 0.079897024_f64;
                }
            } else {
                if input[11] < 0.25804585_f64 {
                    if input[7] < 203.0_f64 {
                        var26 = 0.08011068_f64;
                    } else {
                        var26 = 0.08142334_f64;
                    }
                } else {
                    var26 = 0.07923465_f64;
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.20295984_f64 {
                    var26 = 0.07984664_f64;
                } else {
                    if input[15] < 31.0_f64 {
                        var26 = 0.080892414_f64;
                    } else {
                        var26 = 0.082284175_f64;
                    }
                }
            } else {
                if input[12] < 0.20644216_f64 {
                    if input[12] < 0.12776025_f64 {
                        var26 = 0.08009644_f64;
                    } else {
                        var26 = 0.08200782_f64;
                    }
                } else {
                    if input[7] < 990.0_f64 {
                        var26 = 0.08285582_f64;
                    } else {
                        var26 = 0.0840154_f64;
                    }
                }
            }
        }
    }
    let var27: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 79.0_f64 {
            if input[7] < 46.0_f64 {
                if input[7] < 34.0_f64 {
                    if input[13] < 0.46285716_f64 {
                        var27 = 0.06358605_f64;
                    } else {
                        var27 = 0.023601128_f64;
                    }
                } else {
                    if input[10] < 0.11857708_f64 {
                        var27 = 0.018262513_f64;
                    } else {
                        var27 = 0.06836867_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[29] < 325.0_f64 {
                        var27 = 0.07053807_f64;
                    } else {
                        var27 = 0.03425168_f64;
                    }
                } else {
                    if input[6] < 833.0_f64 {
                        var27 = 0.07273219_f64;
                    } else {
                        var27 = 0.027420191_f64;
                    }
                }
            }
        } else {
            if input[30] < 12.0_f64 {
                if input[7] < 119.0_f64 {
                    if input[6] < 374.0_f64 {
                        var27 = 0.07328587_f64;
                    } else {
                        var27 = 0.06048397_f64;
                    }
                } else {
                    if input[10] < 0.07663783_f64 {
                        var27 = 0.022706129_f64;
                    } else {
                        var27 = 0.07512596_f64;
                    }
                }
            } else {
                if input[7] < 110.0_f64 {
                    if input[12] < 0.14443277_f64 {
                        var27 = 0.07363328_f64;
                    } else {
                        var27 = 0.07576981_f64;
                    }
                } else {
                    var27 = 0.076877914_f64;
                }
            }
        }
    } else {
        if input[7] < 319.0_f64 {
            if input[30] < 14.0_f64 {
                if input[12] < 0.16210526_f64 {
                    if input[5] < 107.0_f64 {
                        var27 = 0.016336996_f64;
                    } else {
                        var27 = 0.07530668_f64;
                    }
                } else {
                    if input[11] < 0.27228683_f64 {
                        var27 = 0.07776188_f64;
                    } else {
                        var27 = 0.075296454_f64;
                    }
                }
            } else {
                if input[12] < 0.14899713_f64 {
                    if input[10] < 0.13926017_f64 {
                        var27 = 0.07081293_f64;
                    } else {
                        var27 = 0.07744857_f64;
                    }
                } else {
                    if input[11] < 0.25531915_f64 {
                        var27 = 0.079389825_f64;
                    } else {
                        var27 = 0.07783457_f64;
                    }
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.20056497_f64 {
                    if input[5] < 80.0_f64 {
                        var27 = 0.025963858_f64;
                    } else {
                        var27 = 0.07826334_f64;
                    }
                } else {
                    if input[15] < 31.0_f64 {
                        var27 = 0.07937048_f64;
                    } else {
                        var27 = 0.08087742_f64;
                    }
                }
            } else {
                if input[7] < 765.0_f64 {
                    if input[12] < 0.185567_f64 {
                        var27 = 0.079631574_f64;
                    } else {
                        var27 = 0.0810938_f64;
                    }
                } else {
                    var27 = 0.08215099_f64;
                }
            }
        }
    }
    let var28: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 73.0_f64 {
            if input[7] < 41.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var28 = 0.0591042_f64;
                    } else {
                        var28 = 0.02224945_f64;
                    }
                } else {
                    if input[11] < 0.36167213_f64 {
                        var28 = 0.06469386_f64;
                    } else {
                        var28 = 0.046659384_f64;
                    }
                }
            } else {
                if input[30] < 13.0_f64 {
                    if input[12] < 0.13622755_f64 {
                        var28 = 0.06620995_f64;
                    } else {
                        var28 = 0.068981305_f64;
                    }
                } else {
                    if input[12] < 0.11165048_f64 {
                        var28 = 0.06768212_f64;
                    } else {
                        var28 = 0.0711549_f64;
                    }
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[7] < 102.0_f64 {
                    if input[11] < 0.29132232_f64 {
                        var28 = 0.071324505_f64;
                    } else {
                        var28 = 0.06698648_f64;
                    }
                } else {
                    if input[12] < 0.15820895_f64 {
                        var28 = 0.07159935_f64;
                    } else {
                        var28 = 0.073740415_f64;
                    }
                }
            } else {
                if input[7] < 110.0_f64 {
                    if input[6] < 470.0_f64 {
                        var28 = 0.07353071_f64;
                    } else {
                        var28 = 0.061230917_f64;
                    }
                } else {
                    var28 = 0.07533641_f64;
                }
            }
        }
    } else {
        if input[7] < 329.0_f64 {
            if input[30] < 15.0_f64 {
                if input[12] < 0.19476268_f64 {
                    if input[11] < 0.34256172_f64 {
                        var28 = 0.07457057_f64;
                    } else {
                        var28 = 0.06908573_f64;
                    }
                } else {
                    if input[30] < 11.0_f64 {
                        var28 = 0.07527217_f64;
                    } else {
                        var28 = 0.07672752_f64;
                    }
                }
            } else {
                if input[11] < 0.25906184_f64 {
                    if input[7] < 203.0_f64 {
                        var28 = 0.07667662_f64;
                    } else {
                        var28 = 0.07813527_f64;
                    }
                } else {
                    if input[0] < 647.0_f64 {
                        var28 = 0.030907622_f64;
                    } else {
                        var28 = 0.0755882_f64;
                    }
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.21534973_f64 {
                    if input[5] < 80.0_f64 {
                        var28 = 0.024749158_f64;
                    } else {
                        var28 = 0.076736525_f64;
                    }
                } else {
                    if input[15] < 30.0_f64 {
                        var28 = 0.07759326_f64;
                    } else {
                        var28 = 0.079369634_f64;
                    }
                }
            } else {
                if input[7] < 765.0_f64 {
                    if input[12] < 0.18503119_f64 {
                        var28 = 0.07793325_f64;
                    } else {
                        var28 = 0.079532735_f64;
                    }
                } else {
                    var28 = 0.080622874_f64;
                }
            }
        }
    }
    let var29: f64;
    if input[7] < 194.0_f64 {
        if input[7] < 89.0_f64 {
            if input[7] < 50.0_f64 {
                if input[7] < 34.0_f64 {
                    if input[13] < 0.46285716_f64 {
                        var29 = 0.058722295_f64;
                    } else {
                        var29 = 0.020961035_f64;
                    }
                } else {
                    if input[10] < 0.11857708_f64 {
                        var29 = 0.013908098_f64;
                    } else {
                        var29 = 0.064326316_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[12] < 0.13118812_f64 {
                        var29 = 0.063084446_f64;
                    } else {
                        var29 = 0.06702234_f64;
                    }
                } else {
                    if input[30] < 18.0_f64 {
                        var29 = 0.068869255_f64;
                    } else {
                        var29 = 0.071501754_f64;
                    }
                }
            }
        } else {
            if input[30] < 13.0_f64 {
                if input[12] < 0.15883978_f64 {
                    if input[5] < 61.0_f64 {
                        var29 = 0.021321272_f64;
                    } else {
                        var29 = 0.0690201_f64;
                    }
                } else {
                    if input[7] < 128.0_f64 {
                        var29 = 0.07054856_f64;
                    } else {
                        var29 = 0.07243207_f64;
                    }
                }
            } else {
                if input[12] < 0.16335227_f64 {
                    if input[7] < 125.0_f64 {
                        var29 = 0.07097436_f64;
                    } else {
                        var29 = 0.07282022_f64;
                    }
                } else {
                    if input[30] < 17.0_f64 {
                        var29 = 0.07332958_f64;
                    } else {
                        var29 = 0.07481807_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 458.0_f64 {
            if input[30] < 15.0_f64 {
                if input[11] < 0.2893082_f64 {
                    if input[12] < 0.2_f64 {
                        var29 = 0.07382938_f64;
                    } else {
                        var29 = 0.075292915_f64;
                    }
                } else {
                    if input[0] < 7051.0_f64 {
                        var29 = 0.07118569_f64;
                    } else {
                        var29 = 0.020536294_f64;
                    }
                }
            } else {
                if input[11] < 0.25804585_f64 {
                    if input[12] < 0.1300813_f64 {
                        var29 = 0.07416382_f64;
                    } else {
                        var29 = 0.07672923_f64;
                    }
                } else {
                    var29 = 0.07443973_f64;
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.22401847_f64 {
                    var29 = 0.075100146_f64;
                } else {
                    if input[11] < 0.25906184_f64 {
                        var29 = 0.07734863_f64;
                    } else {
                        var29 = 0.07261249_f64;
                    }
                }
            } else {
                if input[12] < 0.19248678_f64 {
                    var29 = 0.0769313_f64;
                } else {
                    if input[11] < 0.22365038_f64 {
                        var29 = 0.07908998_f64;
                    } else {
                        var29 = 0.07770138_f64;
                    }
                }
            }
        }
    }
    let var30: f64;
    if input[7] < 194.0_f64 {
        if input[7] < 89.0_f64 {
            if input[7] < 50.0_f64 {
                if input[7] < 34.0_f64 {
                    if input[13] < 0.46285716_f64 {
                        var30 = 0.05622935_f64;
                    } else {
                        var30 = 0.019734746_f64;
                    }
                } else {
                    if input[10] < 0.11857708_f64 {
                        var30 = 0.013225496_f64;
                    } else {
                        var30 = 0.061957177_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[12] < 0.13118812_f64 {
                        var30 = 0.060685057_f64;
                    } else {
                        var30 = 0.06473718_f64;
                    }
                } else {
                    if input[30] < 18.0_f64 {
                        var30 = 0.066650055_f64;
                    } else {
                        var30 = 0.06939122_f64;
                    }
                }
            }
        } else {
            if input[30] < 13.0_f64 {
                if input[12] < 0.15883978_f64 {
                    if input[5] < 61.0_f64 {
                        var30 = 0.020077435_f64;
                    } else {
                        var30 = 0.06680697_f64;
                    }
                } else {
                    if input[7] < 128.0_f64 {
                        var30 = 0.06839622_f64;
                    } else {
                        var30 = 0.07036147_f64;
                    }
                }
            } else {
                if input[12] < 0.16335227_f64 {
                    if input[7] < 125.0_f64 {
                        var30 = 0.06884011_f64;
                    } else {
                        var30 = 0.07076755_f64;
                    }
                } else {
                    if input[30] < 17.0_f64 {
                        var30 = 0.071300566_f64;
                    } else {
                        var30 = 0.07286205_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 458.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.19952267_f64 {
                    if input[8] < 259.0_f64 {
                        var30 = 0.024448706_f64;
                    } else {
                        var30 = 0.070800655_f64;
                    }
                } else {
                    var30 = 0.07291033_f64;
                }
            } else {
                if input[11] < 0.25622255_f64 {
                    if input[7] < 301.0_f64 {
                        var30 = 0.073864274_f64;
                    } else {
                        var30 = 0.07507645_f64;
                    }
                } else {
                    if input[35] < 17.352804_f64 {
                        var30 = 0.031862818_f64;
                    } else {
                        var30 = 0.07229347_f64;
                    }
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.22401847_f64 {
                    var30 = 0.073158495_f64;
                } else {
                    if input[11] < 0.25906184_f64 {
                        var30 = 0.07552731_f64;
                    } else {
                        var30 = 0.07055458_f64;
                    }
                }
            } else {
                if input[12] < 0.19248678_f64 {
                    if input[12] < 0.12776025_f64 {
                        var30 = 0.072973125_f64;
                    } else {
                        var30 = 0.07544656_f64;
                    }
                } else {
                    if input[11] < 0.22365038_f64 {
                        var30 = 0.07736916_f64;
                    } else {
                        var30 = 0.07590004_f64;
                    }
                }
            }
        }
    }
    let var31: f64;
    if input[7] < 189.0_f64 {
        if input[7] < 89.0_f64 {
            if input[7] < 50.0_f64 {
                if input[7] < 34.0_f64 {
                    if input[35] < 17.238165_f64 {
                        var31 = 0.03754179_f64;
                    } else {
                        var31 = 0.053940494_f64;
                    }
                } else {
                    if input[10] < 0.11857708_f64 {
                        var31 = 0.012575218_f64;
                    } else {
                        var31 = 0.059526723_f64;
                    }
                }
            } else {
                if input[30] < 12.0_f64 {
                    if input[12] < 0.14285715_f64 {
                        var31 = 0.059822287_f64;
                    } else {
                        var31 = 0.063032396_f64;
                    }
                } else {
                    if input[12] < 0.17428088_f64 {
                        var31 = 0.06424368_f64;
                    } else {
                        var31 = 0.06633553_f64;
                    }
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.15820895_f64 {
                    if input[5] < 61.0_f64 {
                        var31 = 0.018894773_f64;
                    } else {
                        var31 = 0.064812176_f64;
                    }
                } else {
                    if input[7] < 119.0_f64 {
                        var31 = 0.06614529_f64;
                    } else {
                        var31 = 0.06818448_f64;
                    }
                }
            } else {
                if input[12] < 0.15197569_f64 {
                    if input[7] < 111.0_f64 {
                        var31 = 0.06581887_f64;
                    } else {
                        var31 = 0.06844338_f64;
                    }
                } else {
                    if input[30] < 17.0_f64 {
                        var31 = 0.06911332_f64;
                    } else {
                        var31 = 0.07072523_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 458.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.19952267_f64 {
                    if input[11] < 0.38214287_f64 {
                        var31 = 0.06863412_f64;
                    } else {
                        var31 = 0.052896775_f64;
                    }
                } else {
                    if input[5] < 102.0_f64 {
                        var31 = 0.0664823_f64;
                    } else {
                        var31 = 0.07098846_f64;
                    }
                }
            } else {
                if input[11] < 0.25714287_f64 {
                    if input[7] < 245.0_f64 {
                        var31 = 0.07134331_f64;
                    } else {
                        var31 = 0.07285498_f64;
                    }
                } else {
                    if input[35] < 17.352804_f64 {
                        var31 = 0.040409412_f64;
                    } else {
                        var31 = 0.07013035_f64;
                    }
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.19414414_f64 {
                    var31 = 0.07050926_f64;
                } else {
                    if input[11] < 0.260095_f64 {
                        var31 = 0.073278226_f64;
                    } else {
                        var31 = 0.0698139_f64;
                    }
                }
            } else {
                if input[12] < 0.19248678_f64 {
                    if input[12] < 0.12776025_f64 {
                        var31 = 0.07092901_f64;
                    } else {
                        var31 = 0.07352272_f64;
                    }
                } else {
                    if input[11] < 0.22365038_f64 {
                        var31 = 0.07554885_f64;
                    } else {
                        var31 = 0.074000075_f64;
                    }
                }
            }
        }
    }
    let var32: f64;
    if input[7] < 164.0_f64 {
        if input[7] < 79.0_f64 {
            if input[7] < 44.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[15] < 14.0_f64 {
                        var32 = 0.018790375_f64;
                    } else {
                        var32 = 0.048808604_f64;
                    }
                } else {
                    if input[10] < 0.16041848_f64 {
                        var32 = 0.04361366_f64;
                    } else {
                        var32 = 0.055605598_f64;
                    }
                }
            } else {
                if input[30] < 16.0_f64 {
                    if input[7] < 58.0_f64 {
                        var32 = 0.058250755_f64;
                    } else {
                        var32 = 0.06088992_f64;
                    }
                } else {
                    if input[12] < 0.115189336_f64 {
                        var32 = 0.05972987_f64;
                    } else {
                        var32 = 0.06401579_f64;
                    }
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[7] < 106.0_f64 {
                    if input[11] < 0.25804585_f64 {
                        var32 = 0.06306707_f64;
                    } else {
                        var32 = 0.059991974_f64;
                    }
                } else {
                    if input[10] < 0.37548056_f64 {
                        var32 = 0.06509545_f64;
                    } else {
                        var32 = 0.04747915_f64;
                    }
                }
            } else {
                if input[12] < 0.16783217_f64 {
                    if input[10] < 0.1463964_f64 {
                        var32 = 0.05791818_f64;
                    } else {
                        var32 = 0.065746_f64;
                    }
                } else {
                    var32 = 0.06757678_f64;
                }
            }
        }
    } else {
        if input[7] < 358.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.19354838_f64 {
                    if input[5] < 1883.0_f64 {
                        var32 = 0.065442346_f64;
                    } else {
                        var32 = 0.0018318594_f64;
                    }
                } else {
                    if input[5] < 102.0_f64 {
                        var32 = 0.06314737_f64;
                    } else {
                        var32 = 0.0682578_f64;
                    }
                }
            } else {
                if input[11] < 0.24438202_f64 {
                    if input[7] < 222.0_f64 {
                        var32 = 0.0688345_f64;
                    } else {
                        var32 = 0.070440724_f64;
                    }
                } else {
                    if input[12] < 0.09598741_f64 {
                        var32 = 0.06236977_f64;
                    } else {
                        var32 = 0.06787258_f64;
                    }
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.21595487_f64 {
                    if input[12] < 0.13622755_f64 {
                        var32 = 0.066126816_f64;
                    } else {
                        var32 = 0.06922937_f64;
                    }
                } else {
                    if input[15] < 30.0_f64 {
                        var32 = 0.06972258_f64;
                    } else {
                        var32 = 0.07206582_f64;
                    }
                }
            } else {
                if input[12] < 0.18503119_f64 {
                    if input[12] < 0.12776025_f64 {
                        var32 = 0.06860577_f64;
                    } else {
                        var32 = 0.07129086_f64;
                    }
                } else {
                    if input[7] < 819.0_f64 {
                        var32 = 0.07235571_f64;
                    } else {
                        var32 = 0.07405339_f64;
                    }
                }
            }
        }
    }
    let var33: f64;
    if input[7] < 194.0_f64 {
        if input[7] < 89.0_f64 {
            if input[7] < 50.0_f64 {
                if input[7] < 34.0_f64 {
                    if input[35] < 17.238165_f64 {
                        var33 = 0.032202527_f64;
                    } else {
                        var33 = 0.048791837_f64;
                    }
                } else {
                    if input[10] < 0.11857708_f64 {
                        var33 = 0.00907581_f64;
                    } else {
                        var33 = 0.05452863_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[5] < 343.0_f64 {
                        var33 = 0.056757655_f64;
                    } else {
                        var33 = 0.01604676_f64;
                    }
                } else {
                    if input[30] < 18.0_f64 {
                        var33 = 0.059555717_f64;
                    } else {
                        var33 = 0.062675804_f64;
                    }
                }
            }
        } else {
            if input[30] < 13.0_f64 {
                if input[12] < 0.15883978_f64 {
                    if input[5] < 61.0_f64 {
                        var33 = 0.014142767_f64;
                    } else {
                        var33 = 0.059619214_f64;
                    }
                } else {
                    if input[7] < 128.0_f64 {
                        var33 = 0.061438102_f64;
                    } else {
                        var33 = 0.063637055_f64;
                    }
                }
            } else {
                if input[12] < 0.16335227_f64 {
                    if input[12] < 0.09598741_f64 {
                        var33 = 0.05972622_f64;
                    } else {
                        var33 = 0.06360297_f64;
                    }
                } else {
                    if input[30] < 17.0_f64 {
                        var33 = 0.064706296_f64;
                    } else {
                        var33 = 0.06647256_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 549.0_f64 {
            if input[30] < 15.0_f64 {
                if input[11] < 0.2893082_f64 {
                    if input[12] < 0.19887955_f64 {
                        var33 = 0.06535538_f64;
                    } else {
                        var33 = 0.06712874_f64;
                    }
                } else {
                    if input[8] < 221.0_f64 {
                        var33 = 0.02031722_f64;
                    } else {
                        var33 = 0.06240527_f64;
                    }
                }
            } else {
                if input[12] < 0.17199096_f64 {
                    if input[12] < 0.119382024_f64 {
                        var33 = 0.06416757_f64;
                    } else {
                        var33 = 0.06731289_f64;
                    }
                } else {
                    if input[7] < 301.0_f64 {
                        var33 = 0.06807416_f64;
                    } else {
                        var33 = 0.06963304_f64;
                    }
                }
            }
        } else {
            if input[30] < 16.0_f64 {
                if input[12] < 0.16783217_f64 {
                    if input[10] < 0.10353011_f64 {
                        var33 = 0.045070853_f64;
                    } else {
                        var33 = 0.06575977_f64;
                    }
                } else {
                    if input[22] < 5.385421_f64 {
                        var33 = 0.06809596_f64;
                    } else {
                        var33 = 0.07022168_f64;
                    }
                }
            } else {
                if input[11] < 0.26459855_f64 {
                    if input[12] < 0.18401015_f64 {
                        var33 = 0.070071176_f64;
                    } else {
                        var33 = 0.071950085_f64;
                    }
                } else {
                    if input[16] < 27.717241_f64 {
                        var33 = 0.01962035_f64;
                    } else {
                        var33 = 0.06884682_f64;
                    }
                }
            }
        }
    }
    let var34: f64;
    if input[7] < 205.0_f64 {
        if input[7] < 89.0_f64 {
            if input[7] < 46.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[30] < 10.0_f64 {
                        var34 = 0.03768922_f64;
                    } else {
                        var34 = 0.045863543_f64;
                    }
                } else {
                    if input[10] < 0.14310052_f64 {
                        var34 = 0.033790167_f64;
                    } else {
                        var34 = 0.05078761_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[12] < 0.19414414_f64 {
                        var34 = 0.0527681_f64;
                    } else {
                        var34 = 0.056033876_f64;
                    }
                } else {
                    if input[7] < 63.0_f64 {
                        var34 = 0.055374563_f64;
                    } else {
                        var34 = 0.058155995_f64;
                    }
                }
            }
        } else {
            if input[30] < 13.0_f64 {
                if input[12] < 0.15883978_f64 {
                    if input[5] < 61.0_f64 {
                        var34 = 0.013273402_f64;
                    } else {
                        var34 = 0.057288945_f64;
                    }
                } else {
                    if input[7] < 128.0_f64 {
                        var34 = 0.058995314_f64;
                    } else {
                        var34 = 0.061368097_f64;
                    }
                }
            } else {
                if input[12] < 0.14516129_f64 {
                    if input[7] < 111.0_f64 {
                        var34 = 0.05787869_f64;
                    } else {
                        var34 = 0.061029293_f64;
                    }
                } else {
                    if input[7] < 125.0_f64 {
                        var34 = 0.061463606_f64;
                    } else {
                        var34 = 0.0635688_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 549.0_f64 {
            if input[30] < 15.0_f64 {
                if input[11] < 0.29132232_f64 {
                    if input[12] < 0.20465116_f64 {
                        var34 = 0.063196294_f64;
                    } else {
                        var34 = 0.06502558_f64;
                    }
                } else {
                    if input[0] < 7051.0_f64 {
                        var34 = 0.05994625_f64;
                    } else {
                        var34 = 0.0063986266_f64;
                    }
                }
            } else {
                if input[12] < 0.17943697_f64 {
                    if input[12] < 0.119382024_f64 {
                        var34 = 0.062134165_f64;
                    } else {
                        var34 = 0.065200455_f64;
                    }
                } else {
                    if input[11] < 0.25714287_f64 {
                        var34 = 0.067244075_f64;
                    } else {
                        var34 = 0.06435429_f64;
                    }
                }
            }
        } else {
            if input[30] < 12.0_f64 {
                if input[11] < 0.3178114_f64 {
                    if input[5] < 138.0_f64 {
                        var34 = 0.029104197_f64;
                    } else {
                        var34 = 0.06553623_f64;
                    }
                } else {
                    if input[26] < 27.391703_f64 {
                        var34 = 0.055266965_f64;
                    } else {
                        var34 = 0.012963136_f64;
                    }
                }
            } else {
                if input[12] < 0.19178082_f64 {
                    if input[30] < 16.0_f64 {
                        var34 = 0.064961195_f64;
                    } else {
                        var34 = 0.067691706_f64;
                    }
                } else {
                    if input[30] < 17.0_f64 {
                        var34 = 0.06835961_f64;
                    } else {
                        var34 = 0.069981925_f64;
                    }
                }
            }
        }
    }
    let var35: f64;
    if input[7] < 205.0_f64 {
        if input[7] < 89.0_f64 {
            if input[7] < 50.0_f64 {
                if input[7] < 34.0_f64 {
                    if input[12] < 0.14356436_f64 {
                        var35 = 0.040833555_f64;
                    } else {
                        var35 = 0.046816602_f64;
                    }
                } else {
                    if input[13] < 0.47155812_f64 {
                        var35 = 0.04945038_f64;
                    } else {
                        var35 = 0.020611517_f64;
                    }
                }
            } else {
                if input[30] < 12.0_f64 {
                    if input[12] < 0.14285715_f64 {
                        var35 = 0.049336206_f64;
                    } else {
                        var35 = 0.053157885_f64;
                    }
                } else {
                    if input[12] < 0.17428088_f64 {
                        var35 = 0.054370146_f64;
                    } else {
                        var35 = 0.056917127_f64;
                    }
                }
            }
        } else {
            if input[30] < 12.0_f64 {
                if input[12] < 0.15883978_f64 {
                    if input[10] < 0.10353011_f64 {
                        var35 = 0.029495029_f64;
                    } else {
                        var35 = 0.05419631_f64;
                    }
                } else {
                    if input[7] < 125.0_f64 {
                        var35 = 0.056029137_f64;
                    } else {
                        var35 = 0.058536_f64;
                    }
                }
            } else {
                if input[12] < 0.14443277_f64 {
                    if input[7] < 110.0_f64 {
                        var35 = 0.05498714_f64;
                    } else {
                        var35 = 0.05828721_f64;
                    }
                } else {
                    if input[7] < 125.0_f64 {
                        var35 = 0.058854457_f64;
                    } else {
                        var35 = 0.06097244_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 549.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.124279834_f64 {
                    if input[5] < 491.0_f64 {
                        var35 = 0.045422908_f64;
                    } else {
                        var35 = 0.056163788_f64;
                    }
                } else {
                    if input[11] < 0.28_f64 {
                        var35 = 0.061555594_f64;
                    } else {
                        var35 = 0.05829623_f64;
                    }
                }
            } else {
                if input[12] < 0.20179372_f64 {
                    if input[11] < 0.28440368_f64 {
                        var35 = 0.06289519_f64;
                    } else {
                        var35 = 0.060270198_f64;
                    }
                } else {
                    if input[11] < 0.25714287_f64 {
                        var35 = 0.06481157_f64;
                    } else {
                        var35 = 0.061596014_f64;
                    }
                }
            }
        } else {
            if input[30] < 12.0_f64 {
                if input[11] < 0.32142857_f64 {
                    if input[5] < 138.0_f64 {
                        var35 = 0.02731487_f64;
                    } else {
                        var35 = 0.0631822_f64;
                    }
                } else {
                    if input[26] < 27.391703_f64 {
                        var35 = 0.05200248_f64;
                    } else {
                        var35 = 0.012160025_f64;
                    }
                }
            } else {
                if input[12] < 0.19178082_f64 {
                    if input[30] < 16.0_f64 {
                        var35 = 0.062610805_f64;
                    } else {
                        var35 = 0.06542971_f64;
                    }
                } else {
                    if input[30] < 17.0_f64 {
                        var35 = 0.06612135_f64;
                    } else {
                        var35 = 0.0678063_f64;
                    }
                }
            }
        }
    }
    let var36: f64;
    if input[7] < 205.0_f64 {
        if input[7] < 89.0_f64 {
            if input[7] < 58.0_f64 {
                if input[7] < 38.0_f64 {
                    if input[20] < 10.793282_f64 {
                        var36 = 0.039368633_f64;
                    } else {
                        var36 = 0.045010787_f64;
                    }
                } else {
                    if input[22] < 4.671156_f64 {
                        var36 = 0.04671466_f64;
                    } else {
                        var36 = 0.04980336_f64;
                    }
                }
            } else {
                if input[30] < 12.0_f64 {
                    if input[5] < 373.0_f64 {
                        var36 = 0.050290722_f64;
                    } else {
                        var36 = 0.018792504_f64;
                    }
                } else {
                    if input[12] < 0.17428088_f64 {
                        var36 = 0.05217749_f64;
                    } else {
                        var36 = 0.054821707_f64;
                    }
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.15625_f64 {
                    if input[11] < 0.115555555_f64 {
                        var36 = 0.040664103_f64;
                    } else {
                        var36 = 0.052997787_f64;
                    }
                } else {
                    if input[7] < 119.0_f64 {
                        var36 = 0.054062545_f64;
                    } else {
                        var36 = 0.05669829_f64;
                    }
                }
            } else {
                if input[12] < 0.16535832_f64 {
                    if input[10] < 0.14970563_f64 {
                        var36 = 0.04749067_f64;
                    } else {
                        var36 = 0.056807894_f64;
                    }
                } else {
                    if input[7] < 128.0_f64 {
                        var36 = 0.057475537_f64;
                    } else {
                        var36 = 0.059421934_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 458.0_f64 {
            if input[30] < 16.0_f64 {
                if input[12] < 0.1971831_f64 {
                    if input[30] < 11.0_f64 {
                        var36 = 0.055313736_f64;
                    } else {
                        var36 = 0.058402844_f64;
                    }
                } else {
                    if input[30] < 12.0_f64 {
                        var36 = 0.058897473_f64;
                    } else {
                        var36 = 0.060939413_f64;
                    }
                }
            } else {
                if input[11] < 0.25804585_f64 {
                    if input[10] < 0.35_f64 {
                        var36 = 0.06225602_f64;
                    } else {
                        var36 = 0.056605678_f64;
                    }
                } else {
                    if input[12] < 0.063964844_f64 {
                        var36 = 0.0395259_f64;
                    } else {
                        var36 = 0.058945794_f64;
                    }
                }
            }
        } else {
            if input[30] < 13.0_f64 {
                if input[12] < 0.22401847_f64 {
                    if input[12] < 0.13622755_f64 {
                        var36 = 0.054914713_f64;
                    } else {
                        var36 = 0.059682693_f64;
                    }
                } else {
                    if input[11] < 0.25804585_f64 {
                        var36 = 0.062409826_f64;
                    } else {
                        var36 = 0.05551071_f64;
                    }
                }
            } else {
                if input[12] < 0.19248678_f64 {
                    if input[22] < 6.441144_f64 {
                        var36 = 0.060638595_f64;
                    } else {
                        var36 = 0.062994204_f64;
                    }
                } else {
                    if input[7] < 990.0_f64 {
                        var36 = 0.0638098_f64;
                    } else {
                        var36 = 0.065659635_f64;
                    }
                }
            }
        }
    }
    let var37: f64;
    if input[7] < 155.0_f64 {
        if input[7] < 64.0_f64 {
            if input[7] < 38.0_f64 {
                if input[16] < 18.790983_f64 {
                    if input[12] < 0.13118812_f64 {
                        var37 = 0.026174206_f64;
                    } else {
                        var37 = 0.039226588_f64;
                    }
                } else {
                    if input[19] < 43.5507_f64 {
                        var37 = 0.018295381_f64;
                    } else {
                        var37 = 0.042108793_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[12] < 0.19067797_f64 {
                        var37 = 0.04253648_f64;
                    } else {
                        var37 = 0.04729209_f64;
                    }
                } else {
                    if input[12] < 0.11165048_f64 {
                        var37 = 0.04366484_f64;
                    } else {
                        var37 = 0.048020516_f64;
                    }
                }
            }
        } else {
            if input[7] < 106.0_f64 {
                if input[30] < 15.0_f64 {
                    if input[12] < 0.13118812_f64 {
                        var37 = 0.04612897_f64;
                    } else {
                        var37 = 0.050073322_f64;
                    }
                } else {
                    if input[12] < 0.14899713_f64 {
                        var37 = 0.05061545_f64;
                    } else {
                        var37 = 0.053644568_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[10] < 0.35634327_f64 {
                        var37 = 0.050951578_f64;
                    } else {
                        var37 = 0.02917705_f64;
                    }
                } else {
                    if input[30] < 16.0_f64 {
                        var37 = 0.053507186_f64;
                    } else {
                        var37 = 0.0555932_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 319.0_f64 {
            if input[30] < 15.0_f64 {
                if input[11] < 0.2734694_f64 {
                    if input[12] < 0.19476268_f64 {
                        var37 = 0.054003067_f64;
                    } else {
                        var37 = 0.0564601_f64;
                    }
                } else {
                    if input[11] < 0.34256172_f64 {
                        var37 = 0.052007314_f64;
                    } else {
                        var37 = 0.044350944_f64;
                    }
                }
            } else {
                if input[12] < 0.14899713_f64 {
                    if input[10] < 0.13652053_f64 {
                        var37 = 0.040961947_f64;
                    } else {
                        var37 = 0.055330236_f64;
                    }
                } else {
                    if input[30] < 18.0_f64 {
                        var37 = 0.05752824_f64;
                    } else {
                        var37 = 0.059396844_f64;
                    }
                }
            }
        } else {
            if input[30] < 16.0_f64 {
                if input[12] < 0.19128329_f64 {
                    if input[30] < 11.0_f64 {
                        var37 = 0.053843122_f64;
                    } else {
                        var37 = 0.05718384_f64;
                    }
                } else {
                    if input[22] < 5.1931043_f64 {
                        var37 = 0.057988282_f64;
                    } else {
                        var37 = 0.06045534_f64;
                    }
                }
            } else {
                if input[7] < 765.0_f64 {
                    if input[11] < 0.25906184_f64 {
                        var37 = 0.06089611_f64;
                    } else {
                        var37 = 0.05789574_f64;
                    }
                } else {
                    if input[11] < 0.30646765_f64 {
                        var37 = 0.063232645_f64;
                    } else {
                        var37 = 0.05692658_f64;
                    }
                }
            }
        }
    }
    let var38: f64;
    if input[7] < 205.0_f64 {
        if input[7] < 84.0_f64 {
            if input[7] < 46.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[30] < 10.0_f64 {
                        var38 = 0.027309993_f64;
                    } else {
                        var38 = 0.03602682_f64;
                    }
                } else {
                    if input[30] < 13.0_f64 {
                        var38 = 0.039260145_f64;
                    } else {
                        var38 = 0.04327878_f64;
                    }
                }
            } else {
                if input[30] < 16.0_f64 {
                    if input[11] < 0.27471566_f64 {
                        var38 = 0.045604583_f64;
                    } else {
                        var38 = 0.041286755_f64;
                    }
                } else {
                    if input[12] < 0.11165048_f64 {
                        var38 = 0.044149756_f64;
                    } else {
                        var38 = 0.0498488_f64;
                    }
                }
            }
        } else {
            if input[30] < 11.0_f64 {
                if input[12] < 0.16465864_f64 {
                    if input[0] < 526.0_f64 {
                        var38 = -0.02352186_f64;
                    } else {
                        var38 = 0.04562011_f64;
                    }
                } else {
                    if input[6] < 387.0_f64 {
                        var38 = 0.04928168_f64;
                    } else {
                        var38 = -0.018126694_f64;
                    }
                }
            } else {
                if input[7] < 128.0_f64 {
                    if input[8] < 581.0_f64 {
                        var38 = 0.05045522_f64;
                    } else {
                        var38 = 0.037072454_f64;
                    }
                } else {
                    if input[11] < 0.3178114_f64 {
                        var38 = 0.053084295_f64;
                    } else {
                        var38 = 0.046821974_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 557.0_f64 {
            if input[30] < 15.0_f64 {
                if input[11] < 0.29132232_f64 {
                    if input[12] < 0.21780303_f64 {
                        var38 = 0.053483527_f64;
                    } else {
                        var38 = 0.055467486_f64;
                    }
                } else {
                    if input[8] < 2534.0_f64 {
                        var38 = 0.04959988_f64;
                    } else {
                        var38 = 0.007964218_f64;
                    }
                }
            } else {
                if input[12] < 0.17943697_f64 {
                    if input[12] < 0.119382024_f64 {
                        var38 = 0.051879432_f64;
                    } else {
                        var38 = 0.055450626_f64;
                    }
                } else {
                    if input[11] < 0.25714287_f64 {
                        var38 = 0.057822414_f64;
                    } else {
                        var38 = 0.054533422_f64;
                    }
                }
            }
        } else {
            if input[30] < 12.0_f64 {
                if input[11] < 0.3178114_f64 {
                    if input[5] < 138.0_f64 {
                        var38 = 0.017918928_f64;
                    } else {
                        var38 = 0.05584977_f64;
                    }
                } else {
                    if input[22] < 6.2262416_f64 {
                        var38 = 0.044285275_f64;
                    } else {
                        var38 = 0.0027041635_f64;
                    }
                }
            } else {
                if input[12] < 0.168435_f64 {
                    if input[30] < 19.0_f64 {
                        var38 = 0.05552889_f64;
                    } else {
                        var38 = 0.06013426_f64;
                    }
                } else {
                    if input[11] < 0.24930875_f64 {
                        var38 = 0.060079157_f64;
                    } else {
                        var38 = 0.05732056_f64;
                    }
                }
            }
        }
    }
    let var39: f64;
    if input[7] < 194.0_f64 {
        if input[7] < 79.0_f64 {
            if input[7] < 44.0_f64 {
                if input[7] < 29.0_f64 {
                    if input[15] < 14.0_f64 {
                        var39 = 0.00091426633_f64;
                    } else {
                        var39 = 0.031399626_f64;
                    }
                } else {
                    if input[10] < 0.16041848_f64 {
                        var39 = 0.02329143_f64;
                    } else {
                        var39 = 0.037892237_f64;
                    }
                }
            } else {
                if input[30] < 16.0_f64 {
                    if input[12] < 0.12893553_f64 {
                        var39 = 0.039171092_f64;
                    } else {
                        var39 = 0.04285602_f64;
                    }
                } else {
                    if input[12] < 0.115189336_f64 {
                        var39 = 0.04156147_f64;
                    } else {
                        var39 = 0.046906453_f64;
                    }
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.1418919_f64 {
                    if input[11] < 0.088716626_f64 {
                        var39 = 0.004667513_f64;
                    } else {
                        var39 = 0.043346506_f64;
                    }
                } else {
                    if input[7] < 119.0_f64 {
                        var39 = 0.045692865_f64;
                    } else {
                        var39 = 0.048476677_f64;
                    }
                }
            } else {
                if input[7] < 116.0_f64 {
                    if input[29] < 276.0_f64 {
                        var39 = 0.048253607_f64;
                    } else {
                        var39 = 0.040563818_f64;
                    }
                } else {
                    if input[11] < 0.29727095_f64 {
                        var39 = 0.05102378_f64;
                    } else {
                        var39 = 0.045942854_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 427.0_f64 {
            if input[11] < 0.24074075_f64 {
                if input[30] < 11.0_f64 {
                    if input[35] < 17.770382_f64 {
                        var39 = 0.04634809_f64;
                    } else {
                        var39 = 0.05086459_f64;
                    }
                } else {
                    if input[30] < 18.0_f64 {
                        var39 = 0.053085882_f64;
                    } else {
                        var39 = 0.05534575_f64;
                    }
                }
            } else {
                if input[30] < 13.0_f64 {
                    if input[11] < 0.38214287_f64 {
                        var39 = 0.04799318_f64;
                    } else {
                        var39 = 0.026215006_f64;
                    }
                } else {
                    if input[11] < 0.2893082_f64 {
                        var39 = 0.051923957_f64;
                    } else {
                        var39 = 0.049145576_f64;
                    }
                }
            }
        } else {
            if input[30] < 16.0_f64 {
                if input[12] < 0.20408164_f64 {
                    if input[12] < 0.080063626_f64 {
                        var39 = 0.033658873_f64;
                    } else {
                        var39 = 0.052249085_f64;
                    }
                } else {
                    if input[22] < 5.385421_f64 {
                        var39 = 0.053446364_f64;
                    } else {
                        var39 = 0.056361664_f64;
                    }
                }
            } else {
                if input[7] < 839.0_f64 {
                    if input[12] < 0.20056497_f64 {
                        var39 = 0.05449715_f64;
                    } else {
                        var39 = 0.05699749_f64;
                    }
                } else {
                    if input[11] < 0.30646765_f64 {
                        var39 = 0.058636606_f64;
                    } else {
                        var39 = 0.05150503_f64;
                    }
                }
            }
        }
    }
    let var40: f64;
    if input[7] < 205.0_f64 {
        if input[7] < 89.0_f64 {
            if input[7] < 58.0_f64 {
                if input[7] < 38.0_f64 {
                    if input[20] < 10.793282_f64 {
                        var40 = 0.02971509_f64;
                    } else {
                        var40 = 0.035280593_f64;
                    }
                } else {
                    if input[10] < 0.1839934_f64 {
                        var40 = 0.032332048_f64;
                    } else {
                        var40 = 0.03844116_f64;
                    }
                }
            } else {
                if input[30] < 12.0_f64 {
                    if input[5] < 373.0_f64 {
                        var40 = 0.040031504_f64;
                    } else {
                        var40 = 0.0072183223_f64;
                    }
                } else {
                    if input[8] < 615.0_f64 {
                        var40 = 0.043189492_f64;
                    } else {
                        var40 = 0.013434418_f64;
                    }
                }
            }
        } else {
            if input[30] < 11.0_f64 {
                if input[12] < 0.16210526_f64 {
                    if input[11] < 0.13968255_f64 {
                        var40 = 0.02937898_f64;
                    } else {
                        var40 = 0.040903926_f64;
                    }
                } else {
                    if input[6] < 387.0_f64 {
                        var40 = 0.044263203_f64;
                    } else {
                        var40 = -0.018706447_f64;
                    }
                }
            } else {
                if input[12] < 0.14443277_f64 {
                    if input[12] < 0.09598741_f64 {
                        var40 = 0.04044453_f64;
                    } else {
                        var40 = 0.04505432_f64;
                    }
                } else {
                    if input[30] < 17.0_f64 {
                        var40 = 0.046836626_f64;
                    } else {
                        var40 = 0.049323156_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 557.0_f64 {
            if input[30] < 16.0_f64 {
                if input[12] < 0.1971831_f64 {
                    if input[12] < 0.124279834_f64 {
                        var40 = 0.043951653_f64;
                    } else {
                        var40 = 0.048185866_f64;
                    }
                } else {
                    if input[30] < 12.0_f64 {
                        var40 = 0.048794597_f64;
                    } else {
                        var40 = 0.051158514_f64;
                    }
                }
            } else {
                if input[11] < 0.25906184_f64 {
                    if input[10] < 0.3075_f64 {
                        var40 = 0.05276407_f64;
                    } else {
                        var40 = 0.048761606_f64;
                    }
                } else {
                    if input[12] < 0.063964844_f64 {
                        var40 = 0.02760082_f64;
                    } else {
                        var40 = 0.049189467_f64;
                    }
                }
            }
        } else {
            if input[30] < 12.0_f64 {
                if input[11] < 0.25_f64 {
                    if input[10] < 0.24009325_f64 {
                        var40 = 0.052533697_f64;
                    } else {
                        var40 = 0.047862343_f64;
                    }
                } else {
                    if input[20] < 17.262295_f64 {
                        var40 = 0.0378793_f64;
                    } else {
                        var40 = 0.04779458_f64;
                    }
                }
            } else {
                if input[12] < 0.168435_f64 {
                    if input[30] < 19.0_f64 {
                        var40 = 0.050370194_f64;
                    } else {
                        var40 = 0.055234976_f64;
                    }
                } else {
                    if input[15] < 36.0_f64 {
                        var40 = 0.05352931_f64;
                    } else {
                        var40 = 0.055685516_f64;
                    }
                }
            }
        }
    }
    let var41: f64;
    if input[7] < 222.0_f64 {
        if input[7] < 104.0_f64 {
            if input[7] < 58.0_f64 {
                if input[7] < 38.0_f64 {
                    if input[16] < 18.382183_f64 {
                        var41 = 0.026271269_f64;
                    } else {
                        var41 = 0.031954776_f64;
                    }
                } else {
                    if input[6] < 84.0_f64 {
                        var41 = 0.03663367_f64;
                    } else {
                        var41 = 0.032855462_f64;
                    }
                }
            } else {
                if input[30] < 12.0_f64 {
                    if input[6] < 399.0_f64 {
                        var41 = 0.038103517_f64;
                    } else {
                        var41 = 0.006684655_f64;
                    }
                } else {
                    if input[12] < 0.14899713_f64 {
                        var41 = 0.039044525_f64;
                    } else {
                        var41 = 0.04222812_f64;
                    }
                }
            }
        } else {
            if input[30] < 11.0_f64 {
                if input[10] < 0.33581847_f64 {
                    if input[11] < 0.21112256_f64 {
                        var41 = 0.042950347_f64;
                    } else {
                        var41 = 0.039427724_f64;
                    }
                } else {
                    if input[12] < 0.07342466_f64 {
                        var41 = -0.027898153_f64;
                    } else {
                        var41 = 0.032506865_f64;
                    }
                }
            } else {
                if input[12] < 0.16335227_f64 {
                    if input[12] < 0.09598741_f64 {
                        var41 = 0.03876144_f64;
                    } else {
                        var41 = 0.043567322_f64;
                    }
                } else {
                    if input[30] < 17.0_f64 {
                        var41 = 0.044990003_f64;
                    } else {
                        var41 = 0.04760701_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 703.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.1300813_f64 {
                    if input[10] < 0.16571428_f64 {
                        var41 = 0.02091475_f64;
                    } else {
                        var41 = 0.040821623_f64;
                    }
                } else {
                    if input[11] < 0.24857685_f64 {
                        var41 = 0.047046363_f64;
                    } else {
                        var41 = 0.043976255_f64;
                    }
                }
            } else {
                if input[12] < 0.20179372_f64 {
                    if input[12] < 0.10803619_f64 {
                        var41 = 0.043351833_f64;
                    } else {
                        var41 = 0.04802142_f64;
                    }
                } else {
                    if input[11] < 0.24291939_f64 {
                        var41 = 0.05064976_f64;
                    } else {
                        var41 = 0.047408722_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.25804585_f64 {
                if input[30] < 17.0_f64 {
                    if input[10] < 0.24390244_f64 {
                        var41 = 0.051840853_f64;
                    } else {
                        var41 = 0.048230127_f64;
                    }
                } else {
                    if input[10] < 0.37548056_f64 {
                        var41 = 0.053952683_f64;
                    } else {
                        var41 = 0.03457617_f64;
                    }
                }
            } else {
                if input[19] < 177.12387_f64 {
                    if input[10] < 0.10353011_f64 {
                        var41 = 0.025979102_f64;
                    } else {
                        var41 = -0.040199734_f64;
                    }
                } else {
                    if input[15] < 37.0_f64 {
                        var41 = 0.04533007_f64;
                    } else {
                        var41 = 0.05002156_f64;
                    }
                }
            }
        }
    }
    let var42: f64;
    if input[7] < 164.0_f64 {
        if input[7] < 71.0_f64 {
            if input[7] < 41.0_f64 {
                if input[22] < 3.9122171_f64 {
                    if input[12] < 0.15049505_f64 {
                        var42 = 0.019415313_f64;
                    } else {
                        var42 = 0.02951853_f64;
                    }
                } else {
                    if input[8] < 197.0_f64 {
                        var42 = 0.030689314_f64;
                    } else {
                        var42 = 0.014780971_f64;
                    }
                }
            } else {
                if input[30] < 16.0_f64 {
                    if input[12] < 0.1300813_f64 {
                        var42 = 0.03097938_f64;
                    } else {
                        var42 = 0.034700125_f64;
                    }
                } else {
                    if input[13] < 0.4256757_f64 {
                        var42 = 0.03875948_f64;
                    } else {
                        var42 = 0.027614841_f64;
                    }
                }
            }
        } else {
            if input[30] < 14.0_f64 {
                if input[12] < 0.1418919_f64 {
                    if input[11] < 0.14344262_f64 {
                        var42 = 0.02004533_f64;
                    } else {
                        var42 = 0.035715263_f64;
                    }
                } else {
                    if input[10] < 0.1549101_f64 {
                        var42 = 0.03498293_f64;
                    } else {
                        var42 = 0.039658584_f64;
                    }
                }
            } else {
                if input[7] < 110.0_f64 {
                    if input[6] < 470.0_f64 {
                        var42 = 0.03995759_f64;
                    } else {
                        var42 = 0.019107267_f64;
                    }
                } else {
                    if input[6] < 305.0_f64 {
                        var42 = 0.042794302_f64;
                    } else {
                        var42 = 0.038835_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 319.0_f64 {
            if input[30] < 16.0_f64 {
                if input[11] < 0.2785235_f64 {
                    if input[12] < 0.19476268_f64 {
                        var42 = 0.041446317_f64;
                    } else {
                        var42 = 0.043970376_f64;
                    }
                } else {
                    if input[26] < 176.9332_f64 {
                        var42 = 0.03801043_f64;
                    } else {
                        var42 = -0.023591002_f64;
                    }
                }
            } else {
                if input[6] < 554.0_f64 {
                    if input[29] < 57.0_f64 {
                        var42 = 0.018482536_f64;
                    } else {
                        var42 = 0.045830023_f64;
                    }
                } else {
                    if input[11] < 0.3506606_f64 {
                        var42 = 0.040618293_f64;
                    } else {
                        var42 = 0.025685156_f64;
                    }
                }
            }
        } else {
            if input[30] < 16.0_f64 {
                if input[12] < 0.21595487_f64 {
                    if input[30] < 11.0_f64 {
                        var42 = 0.041437056_f64;
                    } else {
                        var42 = 0.045039997_f64;
                    }
                } else {
                    if input[15] < 30.0_f64 {
                        var42 = 0.045497447_f64;
                    } else {
                        var42 = 0.048602708_f64;
                    }
                }
            } else {
                if input[7] < 765.0_f64 {
                    if input[11] < 0.22622779_f64 {
                        var42 = 0.048749126_f64;
                    } else {
                        var42 = 0.046123005_f64;
                    }
                } else {
                    if input[11] < 0.31177828_f64 {
                        var42 = 0.050921183_f64;
                    } else {
                        var42 = 0.04279736_f64;
                    }
                }
            }
        }
    }
    let var43: f64;
    if input[7] < 222.0_f64 {
        if input[7] < 104.0_f64 {
            if input[7] < 58.0_f64 {
                if input[22] < 4.7004967_f64 {
                    if input[12] < 0.13118812_f64 {
                        var43 = 0.022261534_f64;
                    } else {
                        var43 = 0.02985457_f64;
                    }
                } else {
                    if input[13] < 0.41038525_f64 {
                        var43 = 0.033365708_f64;
                    } else {
                        var43 = 0.027514726_f64;
                    }
                }
            } else {
                if input[30] < 16.0_f64 {
                    if input[11] < 0.26088542_f64 {
                        var43 = 0.03492299_f64;
                    } else {
                        var43 = 0.031031484_f64;
                    }
                } else {
                    if input[12] < 0.11165048_f64 {
                        var43 = 0.03282324_f64;
                    } else {
                        var43 = 0.038377132_f64;
                    }
                }
            }
        } else {
            if input[30] < 11.0_f64 {
                if input[10] < 0.30397022_f64 {
                    if input[11] < 0.21176471_f64 {
                        var43 = 0.03836075_f64;
                    } else {
                        var43 = 0.034511786_f64;
                    }
                } else {
                    if input[20] < 17.784946_f64 {
                        var43 = 0.030359289_f64;
                    } else {
                        var43 = -0.0077494713_f64;
                    }
                }
            } else {
                if input[12] < 0.16335227_f64 {
                    if input[35] < 17.880209_f64 {
                        var43 = 0.035883993_f64;
                    } else {
                        var43 = 0.039022904_f64;
                    }
                } else {
                    if input[30] < 18.0_f64 {
                        var43 = 0.04017675_f64;
                    } else {
                        var43 = 0.043171015_f64;
                    }
                }
            }
        }
    } else {
        if input[15] < 35.0_f64 {
            if input[12] < 0.20056497_f64 {
                if input[12] < 0.124279834_f64 {
                    if input[12] < 0.063964844_f64 {
                        var43 = 0.010932337_f64;
                    } else {
                        var43 = 0.03656756_f64;
                    }
                } else {
                    if input[10] < 0.15306123_f64 {
                        var43 = 0.037004896_f64;
                    } else {
                        var43 = 0.042066246_f64;
                    }
                }
            } else {
                if input[15] < 30.0_f64 {
                    if input[11] < 0.24857685_f64 {
                        var43 = 0.043071117_f64;
                    } else {
                        var43 = 0.03856362_f64;
                    }
                } else {
                    if input[11] < 0.25270757_f64 {
                        var43 = 0.04556712_f64;
                    } else {
                        var43 = 0.0413951_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.17320575_f64 {
                if input[10] < 0.110275686_f64 {
                    if input[4] < 10162.0_f64 {
                        var43 = 0.033132877_f64;
                    } else {
                        var43 = -0.00085026363_f64;
                    }
                } else {
                    if input[12] < 0.12069428_f64 {
                        var43 = 0.040398862_f64;
                    } else {
                        var43 = 0.04434163_f64;
                    }
                }
            } else {
                if input[11] < 0.22365038_f64 {
                    if input[30] < 17.0_f64 {
                        var43 = 0.046971392_f64;
                    } else {
                        var43 = 0.048971426_f64;
                    }
                } else {
                    if input[5] < 110.0_f64 {
                        var43 = 0.006242081_f64;
                    } else {
                        var43 = 0.04522712_f64;
                    }
                }
            }
        }
    }
    let var44: f64;
    if input[7] < 151.0_f64 {
        if input[7] < 64.0_f64 {
            if input[7] < 38.0_f64 {
                if input[20] < 10.793282_f64 {
                    if input[12] < 0.10969388_f64 {
                        var44 = 0.008109957_f64;
                    } else {
                        var44 = 0.023681542_f64;
                    }
                } else {
                    if input[8] < 197.0_f64 {
                        var44 = 0.027480489_f64;
                    } else {
                        var44 = 0.00989714_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[12] < 0.19067797_f64 {
                        var44 = 0.025147809_f64;
                    } else {
                        var44 = 0.030675748_f64;
                    }
                } else {
                    if input[10] < 0.18523775_f64 {
                        var44 = 0.024157433_f64;
                    } else {
                        var44 = 0.031021519_f64;
                    }
                }
            }
        } else {
            if input[30] < 16.0_f64 {
                if input[11] < 0.2875817_f64 {
                    if input[12] < 0.14516129_f64 {
                        var44 = 0.031241227_f64;
                    } else {
                        var44 = 0.03464524_f64;
                    }
                } else {
                    if input[10] < 0.08773527_f64 {
                        var44 = -0.0012807929_f64;
                    } else {
                        var44 = 0.028987262_f64;
                    }
                }
            } else {
                if input[7] < 98.0_f64 {
                    if input[13] < 0.4273577_f64 {
                        var44 = 0.035540257_f64;
                    } else {
                        var44 = 0.024776198_f64;
                    }
                } else {
                    if input[10] < 0.34461153_f64 {
                        var44 = 0.038183913_f64;
                    } else {
                        var44 = 0.030027533_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 319.0_f64 {
            if input[30] < 16.0_f64 {
                if input[11] < 0.24074075_f64 {
                    if input[10] < 0.305761_f64 {
                        var44 = 0.038639303_f64;
                    } else {
                        var44 = 0.033871572_f64;
                    }
                } else {
                    if input[11] < 0.34256172_f64 {
                        var44 = 0.035413753_f64;
                    } else {
                        var44 = 0.027306227_f64;
                    }
                }
            } else {
                if input[11] < 0.25906184_f64 {
                    if input[10] < 0.3008415_f64 {
                        var44 = 0.04121744_f64;
                    } else {
                        var44 = 0.03781973_f64;
                    }
                } else {
                    if input[12] < 0.080063626_f64 {
                        var44 = 0.024377314_f64;
                    } else {
                        var44 = 0.037413843_f64;
                    }
                }
            }
        } else {
            if input[30] < 13.0_f64 {
                if input[12] < 0.13622755_f64 {
                    if input[10] < 0.13926017_f64 {
                        var44 = 0.013318571_f64;
                    } else {
                        var44 = 0.033809274_f64;
                    }
                } else {
                    if input[11] < 0.3178114_f64 {
                        var44 = 0.040529586_f64;
                    } else {
                        var44 = 0.031570192_f64;
                    }
                }
            } else {
                if input[12] < 0.20644216_f64 {
                    if input[22] < 6.441144_f64 {
                        var44 = 0.04024715_f64;
                    } else {
                        var44 = 0.043006834_f64;
                    }
                } else {
                    if input[15] < 35.0_f64 {
                        var44 = 0.043128267_f64;
                    } else {
                        var44 = 0.04564519_f64;
                    }
                }
            }
        }
    }
    let var45: f64;
    if input[7] < 222.0_f64 {
        if input[7] < 106.0_f64 {
            if input[7] < 58.0_f64 {
                if input[7] < 34.0_f64 {
                    if input[12] < 0.14356436_f64 {
                        var45 = 0.017778944_f64;
                    } else {
                        var45 = 0.02530557_f64;
                    }
                } else {
                    if input[30] < 15.0_f64 {
                        var45 = 0.025465429_f64;
                    } else {
                        var45 = 0.030131584_f64;
                    }
                }
            } else {
                if input[30] < 12.0_f64 {
                    if input[10] < 0.11592958_f64 {
                        var45 = 0.01079971_f64;
                    } else {
                        var45 = 0.028781597_f64;
                    }
                } else {
                    if input[12] < 0.14899713_f64 {
                        var45 = 0.029541442_f64;
                    } else {
                        var45 = 0.032852855_f64;
                    }
                }
            }
        } else {
            if input[30] < 11.0_f64 {
                if input[10] < 0.30397022_f64 {
                    if input[10] < 0.1689441_f64 {
                        var45 = 0.028279675_f64;
                    } else {
                        var45 = 0.03287038_f64;
                    }
                } else {
                    if input[35] < 17.238165_f64 {
                        var45 = 0.008000428_f64;
                    } else {
                        var45 = 0.026277963_f64;
                    }
                }
            } else {
                if input[12] < 0.20930232_f64 {
                    if input[30] < 16.0_f64 {
                        var45 = 0.033252794_f64;
                    } else {
                        var45 = 0.03565337_f64;
                    }
                } else {
                    if input[10] < 0.09894699_f64 {
                        var45 = 0.021795142_f64;
                    } else {
                        var45 = 0.036908224_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 16.0_f64 {
            if input[12] < 0.1971831_f64 {
                if input[30] < 11.0_f64 {
                    if input[5] < 202.0_f64 {
                        var45 = 0.008775298_f64;
                    } else {
                        var45 = 0.03307701_f64;
                    }
                } else {
                    if input[29] < 198.0_f64 {
                        var45 = 0.027202472_f64;
                    } else {
                        var45 = 0.03659766_f64;
                    }
                }
            } else {
                if input[15] < 30.0_f64 {
                    if input[11] < 0.24857685_f64 {
                        var45 = 0.037720192_f64;
                    } else {
                        var45 = 0.033403393_f64;
                    }
                } else {
                    if input[11] < 0.25270757_f64 {
                        var45 = 0.04074871_f64;
                    } else {
                        var45 = 0.036681138_f64;
                    }
                }
            }
        } else {
            if input[7] < 765.0_f64 {
                if input[11] < 0.26459855_f64 {
                    if input[12] < 0.20179372_f64 {
                        var45 = 0.038926557_f64;
                    } else {
                        var45 = 0.04119062_f64;
                    }
                } else {
                    if input[10] < 0.23641305_f64 {
                        var45 = 0.03696417_f64;
                    } else {
                        var45 = 0.030606551_f64;
                    }
                }
            } else {
                if input[11] < 0.31177828_f64 {
                    if input[10] < 0.37548056_f64 {
                        var45 = 0.043506283_f64;
                    } else {
                        var45 = 0.018806549_f64;
                    }
                } else {
                    if input[2] < 99.0_f64 {
                        var45 = 0.035741672_f64;
                    } else {
                        var45 = -0.0111098485_f64;
                    }
                }
            }
        }
    }
    let var46: f64;
    if input[7] < 139.0_f64 {
        if input[7] < 64.0_f64 {
            if input[7] < 38.0_f64 {
                if input[19] < 43.5507_f64 {
                    if input[12] < 0.1300813_f64 {
                        var46 = -0.0042351666_f64;
                    } else {
                        var46 = 0.019206325_f64;
                    }
                } else {
                    if input[12] < 0.10803619_f64 {
                        var46 = 0.01763981_f64;
                    } else {
                        var46 = 0.023495397_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[12] < 0.19067797_f64 {
                        var46 = 0.02120785_f64;
                    } else {
                        var46 = 0.026626343_f64;
                    }
                } else {
                    if input[11] < 0.25187203_f64 {
                        var46 = 0.02736781_f64;
                    } else {
                        var46 = 0.022886025_f64;
                    }
                }
            }
        } else {
            if input[30] < 11.0_f64 {
                if input[10] < 0.3962926_f64 {
                    if input[11] < 0.28282827_f64 {
                        var46 = 0.027576445_f64;
                    } else {
                        var46 = 0.021109212_f64;
                    }
                } else {
                    if input[12] < 0.10382322_f64 {
                        var46 = -0.039877217_f64;
                    } else {
                        var46 = 0.008751364_f64;
                    }
                }
            } else {
                if input[13] < 0.43035862_f64 {
                    if input[11] < 0.2893082_f64 {
                        var46 = 0.031225184_f64;
                    } else {
                        var46 = 0.026527513_f64;
                    }
                } else {
                    if input[11] < 0.260095_f64 {
                        var46 = 0.025822539_f64;
                    } else {
                        var46 = 0.010444673_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 319.0_f64 {
            if input[30] < 13.0_f64 {
                if input[12] < 0.13622755_f64 {
                    if input[11] < 0.088716626_f64 {
                        var46 = -0.030987997_f64;
                    } else {
                        var46 = 0.027292505_f64;
                    }
                } else {
                    if input[10] < 0.13217391_f64 {
                        var46 = 0.026472444_f64;
                    } else {
                        var46 = 0.032625098_f64;
                    }
                }
            } else {
                if input[11] < 0.2656396_f64 {
                    if input[30] < 18.0_f64 {
                        var46 = 0.03442356_f64;
                    } else {
                        var46 = 0.036842093_f64;
                    }
                } else {
                    if input[11] < 0.34256172_f64 {
                        var46 = 0.032077488_f64;
                    } else {
                        var46 = 0.023632485_f64;
                    }
                }
            }
        } else {
            if input[30] < 17.0_f64 {
                if input[12] < 0.21595487_f64 {
                    if input[30] < 11.0_f64 {
                        var46 = 0.031499106_f64;
                    } else {
                        var46 = 0.035424452_f64;
                    }
                } else {
                    if input[22] < 5.2245884_f64 {
                        var46 = 0.035508938_f64;
                    } else {
                        var46 = 0.038640644_f64;
                    }
                }
            } else {
                if input[7] < 839.0_f64 {
                    if input[11] < 0.22622779_f64 {
                        var46 = 0.039237365_f64;
                    } else {
                        var46 = 0.036375962_f64;
                    }
                } else {
                    if input[15] < 31.0_f64 {
                        var46 = 0.011957078_f64;
                    } else {
                        var46 = 0.041578565_f64;
                    }
                }
            }
        }
    }
    let var47: f64;
    if input[7] < 222.0_f64 {
        if input[7] < 106.0_f64 {
            if input[7] < 58.0_f64 {
                if input[22] < 4.7004967_f64 {
                    if input[12] < 0.13118812_f64 {
                        var47 = 0.0149402935_f64;
                    } else {
                        var47 = 0.021945354_f64;
                    }
                } else {
                    if input[13] < 0.41038525_f64 {
                        var47 = 0.025288431_f64;
                    } else {
                        var47 = 0.01935474_f64;
                    }
                }
            } else {
                if input[30] < 16.0_f64 {
                    if input[10] < 0.35_f64 {
                        var47 = 0.025616977_f64;
                    } else {
                        var47 = 0.016128117_f64;
                    }
                } else {
                    if input[6] < 209.0_f64 {
                        var47 = 0.029439664_f64;
                    } else {
                        var47 = 0.02287159_f64;
                    }
                }
            }
        } else {
            if input[30] < 11.0_f64 {
                if input[12] < 0.16605166_f64 {
                    if input[11] < 0.124938026_f64 {
                        var47 = 0.008479097_f64;
                    } else {
                        var47 = 0.02484732_f64;
                    }
                } else {
                    if input[10] < 0.17046413_f64 {
                        var47 = 0.02447592_f64;
                    } else {
                        var47 = 0.029264435_f64;
                    }
                }
            } else {
                if input[12] < 0.20930232_f64 {
                    if input[12] < 0.09598741_f64 {
                        var47 = 0.024092639_f64;
                    } else {
                        var47 = 0.030006615_f64;
                    }
                } else {
                    if input[11] < 0.28440368_f64 {
                        var47 = 0.03237738_f64;
                    } else {
                        var47 = 0.02226717_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 819.0_f64 {
            if input[30] < 13.0_f64 {
                if input[11] < 0.28_f64 {
                    if input[10] < 0.2425871_f64 {
                        var47 = 0.032763995_f64;
                    } else {
                        var47 = 0.029978504_f64;
                    }
                } else {
                    if input[11] < 0.38214287_f64 {
                        var47 = 0.02740317_f64;
                    } else {
                        var47 = 0.008258534_f64;
                    }
                }
            } else {
                if input[11] < 0.24146982_f64 {
                    if input[10] < 0.31132075_f64 {
                        var47 = 0.035411805_f64;
                    } else {
                        var47 = 0.030273974_f64;
                    }
                } else {
                    if input[11] < 0.3506606_f64 {
                        var47 = 0.032624297_f64;
                    } else {
                        var47 = 0.024324179_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.25804585_f64 {
                if input[10] < 0.33200124_f64 {
                    if input[30] < 17.0_f64 {
                        var47 = 0.036737565_f64;
                    } else {
                        var47 = 0.03962249_f64;
                    }
                } else {
                    if input[25] < 0.0033013327_f64 {
                        var47 = 0.030642569_f64;
                    } else {
                        var47 = 0.012074429_f64;
                    }
                }
            } else {
                if input[22] < 4.937772_f64 {
                    if input[12] < 0.21722114_f64 {
                        var47 = 0.028527467_f64;
                    } else {
                        var47 = 0.0039897435_f64;
                    }
                } else {
                    if input[13] < 0.42651758_f64 {
                        var47 = 0.03451694_f64;
                    } else {
                        var47 = 0.020729385_f64;
                    }
                }
            }
        }
    }
    let var48: f64;
    if input[7] < 189.0_f64 {
        if input[7] < 84.0_f64 {
            if input[7] < 44.0_f64 {
                if input[30] < 10.0_f64 {
                    if input[12] < 0.10969388_f64 {
                        var48 = 0.0018656284_f64;
                    } else {
                        var48 = 0.015896408_f64;
                    }
                } else {
                    if input[11] < 0.25443786_f64 {
                        var48 = 0.020681474_f64;
                    } else {
                        var48 = 0.016235735_f64;
                    }
                }
            } else {
                if input[30] < 18.0_f64 {
                    if input[11] < 0.27471566_f64 {
                        var48 = 0.02297591_f64;
                    } else {
                        var48 = 0.018691506_f64;
                    }
                } else {
                    if input[12] < 0.113520406_f64 {
                        var48 = 0.021928225_f64;
                    } else {
                        var48 = 0.028990148_f64;
                    }
                }
            }
        } else {
            if input[30] < 16.0_f64 {
                if input[11] < 0.3178114_f64 {
                    if input[35] < 17.271885_f64 {
                        var48 = 0.019385165_f64;
                    } else {
                        var48 = 0.026492584_f64;
                    }
                } else {
                    if input[13] < 0.41821945_f64 {
                        var48 = 0.019060818_f64;
                    } else {
                        var48 = -0.012226432_f64;
                    }
                }
            } else {
                if input[11] < 0.25187203_f64 {
                    if input[35] < 17.88721_f64 {
                        var48 = 0.02746062_f64;
                    } else {
                        var48 = 0.030678341_f64;
                    }
                } else {
                    if input[11] < 0.3506606_f64 {
                        var48 = 0.02700623_f64;
                    } else {
                        var48 = 0.017071297_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 427.0_f64 {
            if input[11] < 0.2785235_f64 {
                if input[30] < 11.0_f64 {
                    if input[13] < 0.45728898_f64 {
                        var48 = 0.028036265_f64;
                    } else {
                        var48 = 0.0070668655_f64;
                    }
                } else {
                    if input[12] < 0.17378917_f64 {
                        var48 = 0.029412556_f64;
                    } else {
                        var48 = 0.03170332_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[7] < 413.0_f64 {
                        var48 = 0.019803127_f64;
                    } else {
                        var48 = -0.032303285_f64;
                    }
                } else {
                    if input[10] < 0.10353011_f64 {
                        var48 = 0.01854184_f64;
                    } else {
                        var48 = 0.027827496_f64;
                    }
                }
            }
        } else {
            if input[22] < 5.385421_f64 {
                if input[11] < 0.3019608_f64 {
                    if input[10] < 0.33581847_f64 {
                        var48 = 0.031166373_f64;
                    } else {
                        var48 = 0.016177831_f64;
                    }
                } else {
                    if input[4] < 10028.0_f64 {
                        var48 = 0.024160026_f64;
                    } else {
                        var48 = 0.010567374_f64;
                    }
                }
            } else {
                if input[12] < 0.13231552_f64 {
                    if input[1] < 1.6584686_f64 {
                        var48 = -0.0013437471_f64;
                    } else {
                        var48 = 0.028652197_f64;
                    }
                } else {
                    if input[11] < 0.25804585_f64 {
                        var48 = 0.034859844_f64;
                    } else {
                        var48 = 0.031501576_f64;
                    }
                }
            }
        }
    }
    let var49: f64;
    if input[7] < 245.0_f64 {
        if input[7] < 106.0_f64 {
            if input[7] < 63.0_f64 {
                if input[30] < 12.0_f64 {
                    if input[12] < 0.14443277_f64 {
                        var49 = 0.013793572_f64;
                    } else {
                        var49 = 0.019107535_f64;
                    }
                } else {
                    if input[10] < 0.18523775_f64 {
                        var49 = 0.011723792_f64;
                    } else {
                        var49 = 0.021287784_f64;
                    }
                }
            } else {
                if input[11] < 0.29545453_f64 {
                    if input[13] < 0.4027778_f64 {
                        var49 = 0.02377978_f64;
                    } else {
                        var49 = 0.020200389_f64;
                    }
                } else {
                    if input[13] < 0.41821945_f64 {
                        var49 = 0.017937759_f64;
                    } else {
                        var49 = -0.008303176_f64;
                    }
                }
            }
        } else {
            if input[30] < 11.0_f64 {
                if input[0] < 3171.0_f64 {
                    if input[11] < 0.29322034_f64 {
                        var49 = 0.023652954_f64;
                    } else {
                        var49 = 0.017414356_f64;
                    }
                } else {
                    var49 = -0.031391665_f64;
                }
            } else {
                if input[30] < 18.0_f64 {
                    if input[11] < 0.24758454_f64 {
                        var49 = 0.026624372_f64;
                    } else {
                        var49 = 0.024046563_f64;
                    }
                } else {
                    if input[12] < 0.16605166_f64 {
                        var49 = 0.026607037_f64;
                    } else {
                        var49 = 0.029927382_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 17.0_f64 {
            if input[12] < 0.19128329_f64 {
                if input[12] < 0.12776025_f64 {
                    if input[16] < 38.773506_f64 {
                        var49 = 0.022116946_f64;
                    } else {
                        var49 = 0.031799477_f64;
                    }
                } else {
                    if input[5] < 225.0_f64 {
                        var49 = 0.01623152_f64;
                    } else {
                        var49 = 0.027816305_f64;
                    }
                }
            } else {
                if input[11] < 0.24857685_f64 {
                    if input[15] < 30.0_f64 {
                        var49 = 0.028942937_f64;
                    } else {
                        var49 = 0.031550452_f64;
                    }
                } else {
                    if input[22] < 5.137559_f64 {
                        var49 = 0.023340395_f64;
                    } else {
                        var49 = 0.027948571_f64;
                    }
                }
            }
        } else {
            if input[7] < 839.0_f64 {
                if input[11] < 0.31177828_f64 {
                    if input[12] < 0.20179372_f64 {
                        var49 = 0.030063212_f64;
                    } else {
                        var49 = 0.032258015_f64;
                    }
                } else {
                    if input[10] < 0.23703703_f64 {
                        var49 = 0.02537829_f64;
                    } else {
                        var49 = 0.0011644283_f64;
                    }
                }
            } else {
                if input[15] < 31.0_f64 {
                    if input[10] < 0.2976695_f64 {
                        var49 = 0.014667273_f64;
                    } else {
                        var49 = -0.023929186_f64;
                    }
                } else {
                    if input[12] < 0.14285715_f64 {
                        var49 = 0.028298963_f64;
                    } else {
                        var49 = 0.034922555_f64;
                    }
                }
            }
        }
    }
    let var50: f64;
    if input[7] < 146.0_f64 {
        if input[7] < 73.0_f64 {
            if input[7] < 41.0_f64 {
                if input[22] < 3.9122171_f64 {
                    if input[6] < 87.0_f64 {
                        var50 = 0.012044926_f64;
                    } else {
                        var50 = -0.007993848_f64;
                    }
                } else {
                    if input[8] < 197.0_f64 {
                        var50 = 0.016261037_f64;
                    } else {
                        var50 = 0.0017774443_f64;
                    }
                }
            } else {
                if input[6] < 99.0_f64 {
                    if input[10] < 0.30397022_f64 {
                        var50 = 0.020174062_f64;
                    } else {
                        var50 = 0.015360675_f64;
                    }
                } else {
                    if input[10] < 0.18052904_f64 {
                        var50 = 0.0104623465_f64;
                    } else {
                        var50 = 0.017561797_f64;
                    }
                }
            }
        } else {
            if input[30] < 12.0_f64 {
                if input[11] < 0.2875817_f64 {
                    if input[35] < 17.728792_f64 {
                        var50 = 0.016092112_f64;
                    } else {
                        var50 = 0.021412997_f64;
                    }
                } else {
                    if input[10] < 0.10353011_f64 {
                        var50 = -0.0065107928_f64;
                    } else {
                        var50 = 0.014966714_f64;
                    }
                }
            } else {
                if input[12] < 0.09598741_f64 {
                    if input[13] < 0.41955444_f64 {
                        var50 = 0.01883908_f64;
                    } else {
                        var50 = 0.00841553_f64;
                    }
                } else {
                    if input[30] < 17.0_f64 {
                        var50 = 0.022581726_f64;
                    } else {
                        var50 = 0.024976926_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 358.0_f64 {
            if input[11] < 0.24074075_f64 {
                if input[30] < 11.0_f64 {
                    if input[10] < 0.305761_f64 {
                        var50 = 0.023863038_f64;
                    } else {
                        var50 = 0.01561631_f64;
                    }
                } else {
                    if input[30] < 18.0_f64 {
                        var50 = 0.02600548_f64;
                    } else {
                        var50 = 0.02853865_f64;
                    }
                }
            } else {
                if input[11] < 0.34256172_f64 {
                    if input[20] < 16.160343_f64 {
                        var50 = 0.02205024_f64;
                    } else {
                        var50 = 0.024981478_f64;
                    }
                } else {
                    if input[10] < 0.14055482_f64 {
                        var50 = 0.010984426_f64;
                    } else {
                        var50 = 0.021270024_f64;
                    }
                }
            }
        } else {
            if input[30] < 13.0_f64 {
                if input[12] < 0.13622755_f64 {
                    if input[24] < 62505.0_f64 {
                        var50 = 0.012228694_f64;
                    } else {
                        var50 = 0.022287732_f64;
                    }
                } else {
                    if input[11] < 0.32142857_f64 {
                        var50 = 0.026889745_f64;
                    } else {
                        var50 = 0.01758569_f64;
                    }
                }
            } else {
                if input[12] < 0.20644216_f64 {
                    if input[22] < 6.441144_f64 {
                        var50 = 0.026439566_f64;
                    } else {
                        var50 = 0.029190416_f64;
                    }
                } else {
                    if input[7] < 1163.0_f64 {
                        var50 = 0.02984122_f64;
                    } else {
                        var50 = 0.03278141_f64;
                    }
                }
            }
        }
    }
    let var51: f64;
    if input[7] < 128.0_f64 {
        if input[30] < 11.0_f64 {
            if input[12] < 0.13118812_f64 {
                if input[19] < 47.51207_f64 {
                    if input[13] < 0.3423729_f64 {
                        var51 = -0.01853592_f64;
                    } else {
                        var51 = -0.0017794324_f64;
                    }
                } else {
                    if input[10] < 0.35634327_f64 {
                        var51 = 0.012853103_f64;
                    } else {
                        var51 = -0.0030176796_f64;
                    }
                }
            } else {
                if input[11] < 0.3506606_f64 {
                    if input[13] < 0.4054945_f64 {
                        var51 = 0.01788345_f64;
                    } else {
                        var51 = 0.013290192_f64;
                    }
                } else {
                    if input[5] < 80.0_f64 {
                        var51 = -0.01620875_f64;
                    } else {
                        var51 = 0.010134994_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.17320575_f64 {
                if input[29] < 41.0_f64 {
                    if input[13] < 0.34507042_f64 {
                        var51 = -0.014279804_f64;
                    } else {
                        var51 = 0.005819427_f64;
                    }
                } else {
                    if input[12] < 0.10803619_f64 {
                        var51 = 0.015279414_f64;
                    } else {
                        var51 = 0.019268941_f64;
                    }
                }
            } else {
                if input[10] < 0.13652053_f64 {
                    if input[30] < 14.0_f64 {
                        var51 = 0.007129207_f64;
                    } else {
                        var51 = 0.020004742_f64;
                    }
                } else {
                    if input[11] < 0.26459855_f64 {
                        var51 = 0.021913897_f64;
                    } else {
                        var51 = 0.016933307_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 319.0_f64 {
            if input[30] < 16.0_f64 {
                if input[11] < 0.24074075_f64 {
                    if input[10] < 0.2683706_f64 {
                        var51 = 0.023578906_f64;
                    } else {
                        var51 = 0.020361846_f64;
                    }
                } else {
                    if input[33] < 41827.0_f64 {
                        var51 = 0.020246318_f64;
                    } else {
                        var51 = 0.012452296_f64;
                    }
                }
            } else {
                if input[12] < 0.1473772_f64 {
                    if input[10] < 0.13652053_f64 {
                        var51 = 0.002925767_f64;
                    } else {
                        var51 = 0.022322252_f64;
                    }
                } else {
                    if input[6] < 52.0_f64 {
                        var51 = 0.008063312_f64;
                    } else {
                        var51 = 0.025312642_f64;
                    }
                }
            }
        } else {
            if input[30] < 12.0_f64 {
                if input[12] < 0.15118197_f64 {
                    if input[10] < 0.13926017_f64 {
                        var51 = -0.00021361785_f64;
                    } else {
                        var51 = 0.01928544_f64;
                    }
                } else {
                    if input[11] < 0.3178114_f64 {
                        var51 = 0.02432031_f64;
                    } else {
                        var51 = 0.014845152_f64;
                    }
                }
            } else {
                if input[12] < 0.20644216_f64 {
                    if input[22] < 6.441144_f64 {
                        var51 = 0.024250934_f64;
                    } else {
                        var51 = 0.027074367_f64;
                    }
                } else {
                    if input[15] < 35.0_f64 {
                        var51 = 0.02689748_f64;
                    } else {
                        var51 = 0.02939766_f64;
                    }
                }
            }
        }
    }
    let var52: f64;
    if input[7] < 222.0_f64 {
        if input[7] < 89.0_f64 {
            if input[30] < 14.0_f64 {
                if input[12] < 0.13718492_f64 {
                    if input[33] < 3948.0_f64 {
                        var52 = -0.005120458_f64;
                    } else {
                        var52 = 0.0122408895_f64;
                    }
                } else {
                    if input[13] < 0.4054945_f64 {
                        var52 = 0.016368708_f64;
                    } else {
                        var52 = 0.012579006_f64;
                    }
                }
            } else {
                if input[8] < 615.0_f64 {
                    if input[11] < 0.25270757_f64 {
                        var52 = 0.019124389_f64;
                    } else {
                        var52 = 0.015648454_f64;
                    }
                } else {
                    if input[5] < 442.0_f64 {
                        var52 = -0.021626411_f64;
                    } else {
                        var52 = 0.00728731_f64;
                    }
                }
            }
        } else {
            if input[30] < 16.0_f64 {
                if input[12] < 0.14356436_f64 {
                    if input[11] < 0.113788486_f64 {
                        var52 = -0.003969894_f64;
                    } else {
                        var52 = 0.016368184_f64;
                    }
                } else {
                    if input[10] < 0.1519871_f64 {
                        var52 = 0.015972724_f64;
                    } else {
                        var52 = 0.020148955_f64;
                    }
                }
            } else {
                if input[12] < 0.168435_f64 {
                    if input[10] < 0.14757554_f64 {
                        var52 = 0.009377236_f64;
                    } else {
                        var52 = 0.020369938_f64;
                    }
                } else {
                    if input[11] < 0.08375_f64 {
                        var52 = 0.009990714_f64;
                    } else {
                        var52 = 0.022757271_f64;
                    }
                }
            }
        }
    } else {
        if input[15] < 36.0_f64 {
            if input[11] < 0.23636363_f64 {
                if input[10] < 0.31335953_f64 {
                    if input[15] < 28.0_f64 {
                        var52 = 0.021897623_f64;
                    } else {
                        var52 = 0.024624957_f64;
                    }
                } else {
                    if input[24] < 28989.0_f64 {
                        var52 = 0.010495802_f64;
                    } else {
                        var52 = 0.018618584_f64;
                    }
                }
            } else {
                if input[30] < 11.0_f64 {
                    if input[11] < 0.29322034_f64 {
                        var52 = 0.019342382_f64;
                    } else {
                        var52 = 0.012986058_f64;
                    }
                } else {
                    if input[10] < 0.15306123_f64 {
                        var52 = 0.019426852_f64;
                    } else {
                        var52 = 0.022444976_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.17320575_f64 {
                if input[10] < 0.110275686_f64 {
                    if input[4] < 10162.0_f64 {
                        var52 = 0.012240372_f64;
                    } else {
                        var52 = -0.022565007_f64;
                    }
                } else {
                    if input[12] < 0.080063626_f64 {
                        var52 = 0.013581865_f64;
                    } else {
                        var52 = 0.023941966_f64;
                    }
                }
            } else {
                if input[11] < 0.22882883_f64 {
                    if input[12] < 0.2877698_f64 {
                        var52 = 0.027243553_f64;
                    } else {
                        var52 = 0.03064093_f64;
                    }
                } else {
                    if input[11] < 0.31177828_f64 {
                        var52 = 0.025376692_f64;
                    } else {
                        var52 = 0.01807635_f64;
                    }
                }
            }
        }
    }
    let var53: f64;
    if input[7] < 245.0_f64 {
        if input[7] < 115.0_f64 {
            if input[7] < 63.0_f64 {
                if input[30] < 16.0_f64 {
                    if input[12] < 0.13231552_f64 {
                        var53 = 0.009805613_f64;
                    } else {
                        var53 = 0.013448797_f64;
                    }
                } else {
                    if input[16] < 28.528854_f64 {
                        var53 = 0.017632842_f64;
                    } else {
                        var53 = 0.0022531503_f64;
                    }
                }
            } else {
                if input[30] < 10.0_f64 {
                    if input[8] < 310.0_f64 {
                        var53 = 0.013801433_f64;
                    } else {
                        var53 = -0.0003664226_f64;
                    }
                } else {
                    if input[13] < 0.42833108_f64 {
                        var53 = 0.017077109_f64;
                    } else {
                        var53 = 0.011386573_f64;
                    }
                }
            }
        } else {
            if input[30] < 11.0_f64 {
                if input[10] < 0.30397022_f64 {
                    if input[10] < 0.16962588_f64 {
                        var53 = 0.013278264_f64;
                    } else {
                        var53 = 0.017932734_f64;
                    }
                } else {
                    if input[1] < 3.973512_f64 {
                        var53 = -0.0014408987_f64;
                    } else {
                        var53 = 0.012395262_f64;
                    }
                }
            } else {
                if input[12] < 0.22857143_f64 {
                    if input[13] < 0.39587975_f64 {
                        var53 = 0.019672997_f64;
                    } else {
                        var53 = 0.017389467_f64;
                    }
                } else {
                    if input[11] < 0.21859904_f64 {
                        var53 = 0.021984814_f64;
                    } else {
                        var53 = 0.017575713_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 17.0_f64 {
            if input[12] < 0.19128329_f64 {
                if input[12] < 0.12541376_f64 {
                    if input[13] < 0.44163424_f64 {
                        var53 = 0.016588118_f64;
                    } else {
                        var53 = 0.00477765_f64;
                    }
                } else {
                    if input[30] < 10.0_f64 {
                        var53 = 0.014849113_f64;
                    } else {
                        var53 = 0.02042575_f64;
                    }
                }
            } else {
                if input[11] < 0.24595469_f64 {
                    if input[15] < 30.0_f64 {
                        var53 = 0.021220729_f64;
                    } else {
                        var53 = 0.023496164_f64;
                    }
                } else {
                    if input[10] < 0.07663783_f64 {
                        var53 = 0.009898508_f64;
                    } else {
                        var53 = 0.019511927_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.2600229_f64 {
                if input[11] < 0.31177828_f64 {
                    if input[12] < 0.119382024_f64 {
                        var53 = 0.017907647_f64;
                    } else {
                        var53 = 0.023622973_f64;
                    }
                } else {
                    if input[10] < 0.23703703_f64 {
                        var53 = 0.017732691_f64;
                    } else {
                        var53 = -0.005532477_f64;
                    }
                }
            } else {
                if input[29] < 1115.0_f64 {
                    if input[10] < 0.21693675_f64 {
                        var53 = 0.02620628_f64;
                    } else {
                        var53 = 0.022823222_f64;
                    }
                } else {
                    if input[3] < 6946.773_f64 {
                        var53 = 0.031990632_f64;
                    } else {
                        var53 = 0.0064873877_f64;
                    }
                }
            }
        }
    }
    let var54: f64;
    if input[7] < 164.0_f64 {
        if input[7] < 78.0_f64 {
            if input[30] < 16.0_f64 {
                if input[12] < 0.12776025_f64 {
                    if input[19] < 47.51207_f64 {
                        var54 = -0.008527881_f64;
                    } else {
                        var54 = 0.010062632_f64;
                    }
                } else {
                    if input[11] < 0.260095_f64 {
                        var54 = 0.013401777_f64;
                    } else {
                        var54 = 0.009524031_f64;
                    }
                }
            } else {
                if input[12] < 0.11165048_f64 {
                    if input[22] < 5.532301_f64 {
                        var54 = 0.019829504_f64;
                    } else {
                        var54 = 0.007683933_f64;
                    }
                } else {
                    if input[16] < 20.977226_f64 {
                        var54 = 0.003433728_f64;
                    } else {
                        var54 = 0.017692426_f64;
                    }
                }
            }
        } else {
            if input[10] < 0.1463964_f64 {
                if input[12] < 0.23616236_f64 {
                    if input[5] < 71.0_f64 {
                        var54 = 0.0031681173_f64;
                    } else {
                        var54 = 0.011614031_f64;
                    }
                } else {
                    if input[20] < 11.595078_f64 {
                        var54 = 0.007892759_f64;
                    } else {
                        var54 = 0.018028807_f64;
                    }
                }
            } else {
                if input[10] < 0.3643846_f64 {
                    if input[13] < 0.42833108_f64 {
                        var54 = 0.016746605_f64;
                    } else {
                        var54 = 0.012422901_f64;
                    }
                } else {
                    if input[2] < 58.0_f64 {
                        var54 = 0.011785901_f64;
                    } else {
                        var54 = -0.003573639_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 409.0_f64 {
            if input[30] < 11.0_f64 {
                if input[13] < 0.45728898_f64 {
                    if input[11] < 0.2785235_f64 {
                        var54 = 0.016554622_f64;
                    } else {
                        var54 = 0.010094657_f64;
                    }
                } else {
                    if input[16] < 24.180304_f64 {
                        var54 = -0.024302742_f64;
                    } else {
                        var54 = 0.0078121214_f64;
                    }
                }
            } else {
                if input[11] < 0.24074075_f64 {
                    if input[12] < 0.20179372_f64 {
                        var54 = 0.018548962_f64;
                    } else {
                        var54 = 0.020578062_f64;
                    }
                } else {
                    if input[10] < 0.110275686_f64 {
                        var54 = 0.010828067_f64;
                    } else {
                        var54 = 0.017534262_f64;
                    }
                }
            }
        } else {
            if input[22] < 5.5213284_f64 {
                if input[12] < 0.12893553_f64 {
                    if input[6] < 920.0_f64 {
                        var54 = -0.016965738_f64;
                    } else {
                        var54 = 0.013227125_f64;
                    }
                } else {
                    if input[10] < 0.110275686_f64 {
                        var54 = 0.01262237_f64;
                    } else {
                        var54 = 0.019939966_f64;
                    }
                }
            } else {
                if input[12] < 0.16402878_f64 {
                    if input[10] < 0.110275686_f64 {
                        var54 = 0.00024142934_f64;
                    } else {
                        var54 = 0.019619077_f64;
                    }
                } else {
                    if input[11] < 0.22691293_f64 {
                        var54 = 0.023079528_f64;
                    } else {
                        var54 = 0.020547235_f64;
                    }
                }
            }
        }
    }
    let var55: f64;
    if input[7] < 245.0_f64 {
        if input[7] < 116.0_f64 {
            if input[30] < 10.0_f64 {
                if input[7] < 115.0_f64 {
                    if input[8] < 310.0_f64 {
                        var55 = 0.010134193_f64;
                    } else {
                        var55 = -0.0017440965_f64;
                    }
                } else {
                    if input[10] < 0.17830883_f64 {
                        var55 = -0.00049174554_f64;
                    } else {
                        var55 = -0.06555852_f64;
                    }
                }
            } else {
                if input[12] < 0.1418919_f64 {
                    if input[5] < 61.0_f64 {
                        var55 = -0.000583132_f64;
                    } else {
                        var55 = 0.011853422_f64;
                    }
                } else {
                    if input[30] < 16.0_f64 {
                        var55 = 0.013483331_f64;
                    } else {
                        var55 = 0.016495448_f64;
                    }
                }
            }
        } else {
            if input[30] < 15.0_f64 {
                if input[12] < 0.15625_f64 {
                    if input[11] < 0.107586205_f64 {
                        var55 = -0.0059892773_f64;
                    } else {
                        var55 = 0.012860457_f64;
                    }
                } else {
                    if input[10] < 0.110275686_f64 {
                        var55 = 0.006770514_f64;
                    } else {
                        var55 = 0.015743189_f64;
                    }
                }
            } else {
                if input[13] < 0.2934363_f64 {
                    if input[10] < 0.17680827_f64 {
                        var55 = 0.0261896_f64;
                    } else {
                        var55 = 0.007899395_f64;
                    }
                } else {
                    if input[13] < 0.42390525_f64 {
                        var55 = 0.017696397_f64;
                    } else {
                        var55 = 0.013987171_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 18.0_f64 {
            if input[12] < 0.22336842_f64 {
                if input[10] < 0.3643846_f64 {
                    if input[30] < 10.0_f64 {
                        var55 = 0.012593269_f64;
                    } else {
                        var55 = 0.017511124_f64;
                    }
                } else {
                    if input[26] < 56.18348_f64 {
                        var55 = 0.0072447606_f64;
                    } else {
                        var55 = -0.03083621_f64;
                    }
                }
            } else {
                if input[10] < 0.26643598_f64 {
                    if input[11] < 0.22691293_f64 {
                        var55 = 0.020367974_f64;
                    } else {
                        var55 = 0.01697188_f64;
                    }
                } else {
                    if input[13] < 0.39709917_f64 {
                        var55 = 0.014199316_f64;
                    } else {
                        var55 = -0.0038804275_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.26459855_f64 {
                if input[7] < 493.0_f64 {
                    if input[0] < 3116.0_f64 {
                        var55 = 0.020243166_f64;
                    } else {
                        var55 = 0.011770754_f64;
                    }
                } else {
                    if input[12] < 0.24329026_f64 {
                        var55 = 0.021557327_f64;
                    } else {
                        var55 = 0.024140337_f64;
                    }
                }
            } else {
                if input[7] < 1047.0_f64 {
                    if input[11] < 0.36167213_f64 {
                        var55 = 0.016862746_f64;
                    } else {
                        var55 = 0.004557377_f64;
                    }
                } else {
                    if input[26] < 2.9937801_f64 {
                        var55 = 0.0050844587_f64;
                    } else {
                        var55 = 0.024357006_f64;
                    }
                }
            }
        }
    }
    let var56: f64;
    if input[7] < 128.0_f64 {
        if input[30] < 10.0_f64 {
            if input[8] < 310.0_f64 {
                if input[11] < 0.36167213_f64 {
                    if input[2] < 94.0_f64 {
                        var56 = 0.008666621_f64;
                    } else {
                        var56 = 0.016369283_f64;
                    }
                } else {
                    if input[7] < 64.0_f64 {
                        var56 = -0.040230837_f64;
                    } else {
                        var56 = 0.008240265_f64;
                    }
                }
            } else {
                if input[11] < 0.19019139_f64 {
                    if input[7] < 72.0_f64 {
                        var56 = 0.027453626_f64;
                    } else {
                        var56 = -0.022800012_f64;
                    }
                } else {
                    if input[8] < 330.0_f64 {
                        var56 = -0.018711606_f64;
                    } else {
                        var56 = 0.006429599_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.1871969_f64 {
                if input[29] < 41.0_f64 {
                    if input[3] < 5001.6816_f64 {
                        var56 = 0.0041219373_f64;
                    } else {
                        var56 = -0.010487179_f64;
                    }
                } else {
                    if input[29] < 316.0_f64 {
                        var56 = 0.011987096_f64;
                    } else {
                        var56 = 0.004520602_f64;
                    }
                }
            } else {
                if input[10] < 0.13926017_f64 {
                    if input[35] < 18.84348_f64 {
                        var56 = 0.0043323967_f64;
                    } else {
                        var56 = 0.016143879_f64;
                    }
                } else {
                    if input[30] < 13.0_f64 {
                        var56 = 0.0131506985_f64;
                    } else {
                        var56 = 0.015476092_f64;
                    }
                }
            }
        }
    } else {
        if input[15] < 30.0_f64 {
            if input[12] < 0.20179372_f64 {
                if input[35] < 17.238165_f64 {
                    if input[4] < 11465.0_f64 {
                        var56 = 0.0070274593_f64;
                    } else {
                        var56 = -0.02015123_f64;
                    }
                } else {
                    if input[10] < 0.15306123_f64 {
                        var56 = 0.008477144_f64;
                    } else {
                        var56 = 0.013912357_f64;
                    }
                }
            } else {
                if input[10] < 0.1486048_f64 {
                    if input[12] < 0.27208757_f64 {
                        var56 = 0.010765244_f64;
                    } else {
                        var56 = 0.01487483_f64;
                    }
                } else {
                    if input[10] < 0.24460432_f64 {
                        var56 = 0.017192071_f64;
                    } else {
                        var56 = 0.0137369605_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.16605166_f64 {
                if input[10] < 0.14970563_f64 {
                    if input[12] < 0.08512975_f64 {
                        var56 = -0.021995803_f64;
                    } else {
                        var56 = 0.01000235_f64;
                    }
                } else {
                    if input[10] < 0.35_f64 {
                        var56 = 0.016004711_f64;
                    } else {
                        var56 = 0.009344149_f64;
                    }
                }
            } else {
                if input[7] < 990.0_f64 {
                    if input[10] < 0.33200124_f64 {
                        var56 = 0.01768875_f64;
                    } else {
                        var56 = 0.010723299_f64;
                    }
                } else {
                    if input[10] < 0.07663783_f64 {
                        var56 = 0.009022137_f64;
                    } else {
                        var56 = 0.020563604_f64;
                    }
                }
            }
        }
    }
    let var57: f64;
    if input[7] < 266.0_f64 {
        if input[7] < 104.0_f64 {
            if input[30] < 18.0_f64 {
                if input[11] < 0.26183686_f64 {
                    if input[10] < 0.31768888_f64 {
                        var57 = 0.011047565_f64;
                    } else {
                        var57 = 0.006807799_f64;
                    }
                } else {
                    if input[13] < 0.41384995_f64 {
                        var57 = 0.0077762986_f64;
                    } else {
                        var57 = -0.0010486348_f64;
                    }
                }
            } else {
                if input[2] < 93.0_f64 {
                    if input[11] < 0.0931677_f64 {
                        var57 = -0.0054736338_f64;
                    } else {
                        var57 = 0.015209344_f64;
                    }
                } else {
                    if input[35] < 17.957962_f64 {
                        var57 = -0.011083856_f64;
                    } else {
                        var57 = 0.011914506_f64;
                    }
                }
            }
        } else {
            if input[30] < 18.0_f64 {
                if input[35] < 17.271885_f64 {
                    if input[10] < 0.28091604_f64 {
                        var57 = 0.010128179_f64;
                    } else {
                        var57 = -0.0061189677_f64;
                    }
                } else {
                    if input[11] < 0.24220484_f64 {
                        var57 = 0.013577856_f64;
                    } else {
                        var57 = 0.01123772_f64;
                    }
                }
            } else {
                if input[8] < 663.0_f64 {
                    if input[35] < 18.95267_f64 {
                        var57 = 0.016431594_f64;
                    } else {
                        var57 = 0.012512398_f64;
                    }
                } else {
                    if input[6] < 379.0_f64 {
                        var57 = 0.000836173_f64;
                    } else {
                        var57 = 0.011571525_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 11.0_f64 {
            if input[12] < 0.13622755_f64 {
                if input[22] < 6.2262416_f64 {
                    if input[11] < 0.15488656_f64 {
                        var57 = -0.02370096_f64;
                    } else {
                        var57 = 0.004408499_f64;
                    }
                } else {
                    if input[6] < 2197.0_f64 {
                        var57 = 0.029946698_f64;
                    } else {
                        var57 = -0.007663087_f64;
                    }
                }
            } else {
                if input[11] < 0.30646765_f64 {
                    if input[35] < 17.84448_f64 {
                        var57 = 0.010214443_f64;
                    } else {
                        var57 = 0.014498303_f64;
                    }
                } else {
                    if input[8] < 438.0_f64 {
                        var57 = -0.029549053_f64;
                    } else {
                        var57 = 0.0072238706_f64;
                    }
                }
            }
        } else {
            if input[7] < 703.0_f64 {
                if input[12] < 0.124279834_f64 {
                    if input[19] < 405.7972_f64 {
                        var57 = 0.011638749_f64;
                    } else {
                        var57 = -0.018615358_f64;
                    }
                } else {
                    if input[10] < 0.15306123_f64 {
                        var57 = 0.013853523_f64;
                    } else {
                        var57 = 0.016324174_f64;
                    }
                }
            } else {
                if input[11] < 0.30880615_f64 {
                    if input[10] < 0.31768888_f64 {
                        var57 = 0.018434083_f64;
                    } else {
                        var57 = 0.011566197_f64;
                    }
                } else {
                    if input[16] < 34.75925_f64 {
                        var57 = -0.0039828173_f64;
                    } else {
                        var57 = 0.013254272_f64;
                    }
                }
            }
        }
    }
    let var58: f64;
    if input[7] < 245.0_f64 {
        if input[30] < 13.0_f64 {
            if input[12] < 0.13622755_f64 {
                if input[19] < 50.294167_f64 {
                    if input[13] < 0.3423729_f64 {
                        var58 = -0.020660609_f64;
                    } else {
                        var58 = -0.0026862652_f64;
                    }
                } else {
                    if input[11] < 0.088716626_f64 {
                        var58 = -0.03540901_f64;
                    } else {
                        var58 = 0.007081496_f64;
                    }
                }
            } else {
                if input[7] < 119.0_f64 {
                    if input[35] < 17.728792_f64 {
                        var58 = 0.005387363_f64;
                    } else {
                        var58 = 0.009572381_f64;
                    }
                } else {
                    if input[10] < 0.13217391_f64 {
                        var58 = 0.005700987_f64;
                    } else {
                        var58 = 0.011769808_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.171415_f64 {
                if input[15] < 28.0_f64 {
                    if input[10] < 0.16133004_f64 {
                        var58 = 0.00073397387_f64;
                    } else {
                        var58 = 0.009551708_f64;
                    }
                } else {
                    if input[12] < 0.09598741_f64 {
                        var58 = 0.007742207_f64;
                    } else {
                        var58 = 0.012562816_f64;
                    }
                }
            } else {
                if input[11] < 0.2256_f64 {
                    if input[10] < 0.35_f64 {
                        var58 = 0.013918805_f64;
                    } else {
                        var58 = 0.00012015095_f64;
                    }
                } else {
                    if input[19] < 160.84395_f64 {
                        var58 = 0.011201387_f64;
                    } else {
                        var58 = 0.022669647_f64;
                    }
                }
            }
        }
    } else {
        if input[15] < 37.0_f64 {
            if input[11] < 0.23636363_f64 {
                if input[10] < 0.29475984_f64 {
                    if input[13] < 0.41821945_f64 {
                        var58 = 0.015503304_f64;
                    } else {
                        var58 = 0.012281265_f64;
                    }
                } else {
                    if input[10] < 0.3394348_f64 {
                        var58 = 0.0119736_f64;
                    } else {
                        var58 = 0.0062660086_f64;
                    }
                }
            } else {
                if input[11] < 0.30880615_f64 {
                    if input[35] < 17.908493_f64 {
                        var58 = 0.0076485686_f64;
                    } else {
                        var58 = 0.012826348_f64;
                    }
                } else {
                    if input[10] < 0.110275686_f64 {
                        var58 = 0.0028601713_f64;
                    } else {
                        var58 = 0.010299814_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.2877698_f64 {
                if input[12] < 0.12069428_f64 {
                    if input[35] < 17.238165_f64 {
                        var58 = -0.00033671357_f64;
                    } else {
                        var58 = 0.012546616_f64;
                    }
                } else {
                    if input[29] < 221.0_f64 {
                        var58 = 0.0077095027_f64;
                    } else {
                        var58 = 0.016542148_f64;
                    }
                }
            } else {
                if input[1] < 7.2376733_f64 {
                    if input[24] < 161555.0_f64 {
                        var58 = 0.02247397_f64;
                    } else {
                        var58 = -0.0016616964_f64;
                    }
                } else {
                    if input[10] < 0.09894699_f64 {
                        var58 = -0.0017630684_f64;
                    } else {
                        var58 = 0.017405411_f64;
                    }
                }
            }
        }
    }
    let var59: f64;
    if input[7] < 139.0_f64 {
        if input[30] < 11.0_f64 {
            if input[10] < 0.32578397_f64 {
                if input[12] < 0.19665273_f64 {
                    if input[5] < 82.0_f64 {
                        var59 = 0.0033112105_f64;
                    } else {
                        var59 = 0.0076559368_f64;
                    }
                } else {
                    if input[15] < 28.0_f64 {
                        var59 = 0.009673673_f64;
                    } else {
                        var59 = -0.009327488_f64;
                    }
                }
            } else {
                if input[5] < 458.0_f64 {
                    if input[1] < 3.1898355_f64 {
                        var59 = -0.021503152_f64;
                    } else {
                        var59 = 0.0026925376_f64;
                    }
                } else {
                    if input[15] < 28.0_f64 {
                        var59 = 0.0020211863_f64;
                    } else {
                        var59 = -0.04800799_f64;
                    }
                }
            }
        } else {
            if input[13] < 0.42833108_f64 {
                if input[11] < 0.24074075_f64 {
                    if input[10] < 0.2831126_f64 {
                        var59 = 0.011656835_f64;
                    } else {
                        var59 = 0.008622553_f64;
                    }
                } else {
                    if input[5] < 100.0_f64 {
                        var59 = 0.0061007724_f64;
                    } else {
                        var59 = 0.009669849_f64;
                    }
                }
            } else {
                if input[10] < 0.15960912_f64 {
                    if input[12] < 0.15749696_f64 {
                        var59 = -0.015148546_f64;
                    } else {
                        var59 = 0.00467045_f64;
                    }
                } else {
                    if input[10] < 0.26_f64 {
                        var59 = 0.00830764_f64;
                    } else {
                        var59 = -0.0017757891_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 17.0_f64 {
            if input[12] < 0.22401847_f64 {
                if input[11] < 0.123484015_f64 {
                    if input[12] < 0.11165048_f64 {
                        var59 = -0.0136753395_f64;
                    } else {
                        var59 = 0.006942673_f64;
                    }
                } else {
                    if input[5] < 124.0_f64 {
                        var59 = 0.003453362_f64;
                    } else {
                        var59 = 0.011357727_f64;
                    }
                }
            } else {
                if input[10] < 0.26643598_f64 {
                    if input[19] < 176.25294_f64 {
                        var59 = 0.0125962645_f64;
                    } else {
                        var59 = 0.015252091_f64;
                    }
                } else {
                    if input[7] < 143.0_f64 {
                        var59 = -0.019628882_f64;
                    } else {
                        var59 = 0.007868916_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.2692793_f64 {
                if input[7] < 765.0_f64 {
                    if input[13] < 0.4041451_f64 {
                        var59 = 0.013834319_f64;
                    } else {
                        var59 = 0.011299365_f64;
                    }
                } else {
                    if input[10] < 0.37548056_f64 {
                        var59 = 0.016018549_f64;
                    } else {
                        var59 = -0.016695017_f64;
                    }
                }
            } else {
                if input[5] < 65.0_f64 {
                    var59 = -0.034823313_f64;
                } else {
                    if input[25] < 0.0009489633_f64 {
                        var59 = 0.022363411_f64;
                    } else {
                        var59 = 0.016498407_f64;
                    }
                }
            }
        }
    }
    let var60: f64;
    if input[7] < 266.0_f64 {
        if input[7] < 78.0_f64 {
            if input[12] < 0.09328358_f64 {
                if input[1] < 7.6474423_f64 {
                    if input[1] < 7.476715_f64 {
                        var60 = 0.00047322005_f64;
                    } else {
                        var60 = -0.029817117_f64;
                    }
                } else {
                    if input[20] < 11.754217_f64 {
                        var60 = -0.007654947_f64;
                    } else {
                        var60 = 0.0115704825_f64;
                    }
                }
            } else {
                if input[30] < 18.0_f64 {
                    if input[4] < 10923.0_f64 {
                        var60 = 0.0065373885_f64;
                    } else {
                        var60 = 0.010519108_f64;
                    }
                } else {
                    if input[2] < 93.0_f64 {
                        var60 = 0.012690827_f64;
                    } else {
                        var60 = 0.0017526094_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.3178114_f64 {
                if input[30] < 15.0_f64 {
                    if input[10] < 0.31335953_f64 {
                        var60 = 0.009497269_f64;
                    } else {
                        var60 = 0.005116459_f64;
                    }
                } else {
                    if input[13] < 0.42390525_f64 {
                        var60 = 0.011367655_f64;
                    } else {
                        var60 = 0.007426093_f64;
                    }
                }
            } else {
                if input[22] < 5.1475143_f64 {
                    if input[35] < 18.189157_f64 {
                        var60 = -0.021913601_f64;
                    } else {
                        var60 = 0.0023115382_f64;
                    }
                } else {
                    if input[25] < 0.13048932_f64 {
                        var60 = 0.008168324_f64;
                    } else {
                        var60 = -0.00079830684_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 12.0_f64 {
            if input[30] < 10.0_f64 {
                if input[35] < 17.531393_f64 {
                    if input[22] < 5.5116053_f64 {
                        var60 = -0.006891403_f64;
                    } else {
                        var60 = 0.012956816_f64;
                    }
                } else {
                    if input[11] < 0.3019608_f64 {
                        var60 = 0.009394924_f64;
                    } else {
                        var60 = -0.0000073084775_f64;
                    }
                }
            } else {
                if input[13] < 0.33932462_f64 {
                    if input[6] < 2527.0_f64 {
                        var60 = 0.008666394_f64;
                    } else {
                        var60 = -0.013764086_f64;
                    }
                } else {
                    if input[12] < 0.2320377_f64 {
                        var60 = 0.010237526_f64;
                    } else {
                        var60 = 0.01330975_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.12069428_f64 {
                if input[11] < 0.115555555_f64 {
                    if input[11] < 0.07709251_f64 {
                        var60 = 0.007162083_f64;
                    } else {
                        var60 = -0.024323199_f64;
                    }
                } else {
                    if input[1] < 8.927292_f64 {
                        var60 = 0.009307324_f64;
                    } else {
                        var60 = 0.0011662644_f64;
                    }
                }
            } else {
                if input[15] < 36.0_f64 {
                    if input[13] < 0.41821945_f64 {
                        var60 = 0.0126228435_f64;
                    } else {
                        var60 = 0.0097052315_f64;
                    }
                } else {
                    if input[11] < 0.31177828_f64 {
                        var60 = 0.0143628195_f64;
                    } else {
                        var60 = 0.008351473_f64;
                    }
                }
            }
        }
    }
    let var61: f64;
    if input[7] < 128.0_f64 {
        if input[30] < 10.0_f64 {
            if input[8] < 310.0_f64 {
                if input[2] < 94.0_f64 {
                    if input[11] < 0.36167213_f64 {
                        var61 = 0.0046599745_f64;
                    } else {
                        var61 = -0.02395323_f64;
                    }
                } else {
                    if input[5] < 71.0_f64 {
                        var61 = -0.0018356545_f64;
                    } else {
                        var61 = 0.016854675_f64;
                    }
                }
            } else {
                if input[1] < 5.8652153_f64 {
                    if input[1] < 4.5170293_f64 {
                        var61 = -0.013023153_f64;
                    } else {
                        var61 = 0.011843539_f64;
                    }
                } else {
                    if input[11] < 0.3019608_f64 {
                        var61 = -0.006841492_f64;
                    } else {
                        var61 = -0.03877194_f64;
                    }
                }
            }
        } else {
            if input[8] < 581.0_f64 {
                if input[7] < 63.0_f64 {
                    if input[12] < 0.2320377_f64 {
                        var61 = 0.0057247053_f64;
                    } else {
                        var61 = 0.012878909_f64;
                    }
                } else {
                    if input[13] < 0.43035862_f64 {
                        var61 = 0.008598966_f64;
                    } else {
                        var61 = 0.0039450224_f64;
                    }
                }
            } else {
                if input[5] < 286.0_f64 {
                    if input[1] < 4.485425_f64 {
                        var61 = -0.012815154_f64;
                    } else {
                        var61 = -0.052070923_f64;
                    }
                } else {
                    if input[20] < 17.908752_f64 {
                        var61 = -0.008880707_f64;
                    } else {
                        var61 = 0.009365114_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 18.0_f64 {
            if input[12] < 0.22401847_f64 {
                if input[15] < 28.0_f64 {
                    if input[13] < 0.45338568_f64 {
                        var61 = 0.007887698_f64;
                    } else {
                        var61 = -0.0025404578_f64;
                    }
                } else {
                    if input[10] < 0.31991714_f64 {
                        var61 = 0.010000386_f64;
                    } else {
                        var61 = 0.005647559_f64;
                    }
                }
            } else {
                if input[10] < 0.26643598_f64 {
                    if input[11] < 0.22691293_f64 {
                        var61 = 0.011955876_f64;
                    } else {
                        var61 = 0.008777889_f64;
                    }
                } else {
                    if input[15] < 22.0_f64 {
                        var61 = -0.011139469_f64;
                    } else {
                        var61 = 0.006457222_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.21907601_f64 {
                if input[35] < 17.718607_f64 {
                    if input[6] < 52.0_f64 {
                        var61 = -0.03526097_f64;
                    } else {
                        var61 = 0.010905729_f64;
                    }
                } else {
                    if input[7] < 500.0_f64 {
                        var61 = 0.012852934_f64;
                    } else {
                        var61 = 0.015404916_f64;
                    }
                }
            } else {
                if input[13] < 0.39241052_f64 {
                    if input[10] < 0.29319373_f64 {
                        var61 = 0.011794106_f64;
                    } else {
                        var61 = 0.004490593_f64;
                    }
                } else {
                    if input[22] < 7.023741_f64 {
                        var61 = 0.0068959123_f64;
                    } else {
                        var61 = 0.011883782_f64;
                    }
                }
            }
        }
    }
    let var62: f64;
    if input[15] < 30.0_f64 {
        if input[12] < 0.16666667_f64 {
            if input[5] < 55.0_f64 {
                if input[16] < 23.413408_f64 {
                    if input[13] < 0.34507042_f64 {
                        var62 = -0.013311932_f64;
                    } else {
                        var62 = -0.00027222442_f64;
                    }
                } else {
                    var62 = -0.03258771_f64;
                }
            } else {
                if input[13] < 0.41095892_f64 {
                    if input[10] < 0.31335953_f64 {
                        var62 = 0.00703093_f64;
                    } else {
                        var62 = 0.0040841727_f64;
                    }
                } else {
                    if input[29] < 645.0_f64 {
                        var62 = 0.004034279_f64;
                    } else {
                        var62 = -0.011122133_f64;
                    }
                }
            }
        } else {
            if input[30] < 12.0_f64 {
                if input[10] < 0.1270073_f64 {
                    if input[16] < 30.821146_f64 {
                        var62 = 0.0031977803_f64;
                    } else {
                        var62 = -0.023054907_f64;
                    }
                } else {
                    if input[11] < 0.0931677_f64 {
                        var62 = -0.0007520395_f64;
                    } else {
                        var62 = 0.007673606_f64;
                    }
                }
            } else {
                if input[10] < 0.14970563_f64 {
                    if input[12] < 0.24329026_f64 {
                        var62 = 0.0042318157_f64;
                    } else {
                        var62 = 0.008260327_f64;
                    }
                } else {
                    if input[10] < 0.26643598_f64 {
                        var62 = 0.009960956_f64;
                    } else {
                        var62 = 0.007089101_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.1300813_f64 {
            if input[11] < 0.12880678_f64 {
                if input[22] < 5.5116053_f64 {
                    if input[8] < 555.0_f64 {
                        var62 = 0.0040673576_f64;
                    } else {
                        var62 = -0.0400664_f64;
                    }
                } else {
                    if input[4] < 7652.0_f64 {
                        var62 = 0.0018766964_f64;
                    } else {
                        var62 = -0.019546226_f64;
                    }
                }
            } else {
                if input[10] < 0.14757554_f64 {
                    if input[16] < 34.891605_f64 {
                        var62 = -0.009308777_f64;
                    } else {
                        var62 = 0.011764135_f64;
                    }
                } else {
                    if input[13] < 0.39669928_f64 {
                        var62 = 0.009180877_f64;
                    } else {
                        var62 = 0.005421233_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.28242075_f64 {
                if input[10] < 0.10747664_f64 {
                    if input[11] < 0.36167213_f64 {
                        var62 = 0.006161347_f64;
                    } else {
                        var62 = -0.0069325804_f64;
                    }
                } else {
                    if input[15] < 36.0_f64 {
                        var62 = 0.00977222_f64;
                    } else {
                        var62 = 0.011640572_f64;
                    }
                }
            } else {
                if input[22] < 4.8675985_f64 {
                    if input[11] < 0.1954638_f64 {
                        var62 = 0.026897052_f64;
                    } else {
                        var62 = -0.014216992_f64;
                    }
                } else {
                    if input[25] < 0.00077370566_f64 {
                        var62 = 0.018027095_f64;
                    } else {
                        var62 = 0.012266779_f64;
                    }
                }
            }
        }
    }
    let var63: f64;
    if input[7] < 266.0_f64 {
        if input[30] < 13.0_f64 {
            if input[12] < 0.19414414_f64 {
                if input[19] < 67.94796_f64 {
                    if input[12] < 0.10144927_f64 {
                        var63 = -0.0056176004_f64;
                    } else {
                        var63 = 0.0030659323_f64;
                    }
                } else {
                    if input[10] < 0.19875777_f64 {
                        var63 = 0.0030826072_f64;
                    } else {
                        var63 = 0.0060741_f64;
                    }
                }
            } else {
                if input[10] < 0.13217391_f64 {
                    if input[4] < 13595.0_f64 {
                        var63 = 0.0026464933_f64;
                    } else {
                        var63 = -0.03258748_f64;
                    }
                } else {
                    if input[11] < 0.0931677_f64 {
                        var63 = -0.0011107046_f64;
                    } else {
                        var63 = 0.007647443_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.09598741_f64 {
                if input[10] < 0.14310052_f64 {
                    if input[3] < 5420.476_f64 {
                        var63 = -0.01819119_f64;
                    } else {
                        var63 = 0.009440412_f64;
                    }
                } else {
                    if input[30] < 15.0_f64 {
                        var63 = -0.0007539532_f64;
                    } else {
                        var63 = 0.0052491627_f64;
                    }
                }
            } else {
                if input[35] < 19.480465_f64 {
                    if input[30] < 18.0_f64 {
                        var63 = 0.007576663_f64;
                    } else {
                        var63 = 0.009502678_f64;
                    }
                } else {
                    if input[10] < 0.2961165_f64 {
                        var63 = 0.003949707_f64;
                    } else {
                        var63 = -0.0075826845_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 10.0_f64 {
            if input[11] < 0.07709251_f64 {
                if input[7] < 395.0_f64 {
                    var63 = -0.057200253_f64;
                } else {
                    if input[16] < 26.685286_f64 {
                        var63 = 0.009853357_f64;
                    } else {
                        var63 = -0.014635585_f64;
                    }
                }
            } else {
                if input[13] < 0.44163424_f64 {
                    if input[12] < 0.23616236_f64 {
                        var63 = 0.004328215_f64;
                    } else {
                        var63 = 0.0088424245_f64;
                    }
                } else {
                    if input[22] < 4.2844787_f64 {
                        var63 = -0.04542813_f64;
                    } else {
                        var63 = 0.0004698217_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.25804585_f64 {
                if input[10] < 0.26071286_f64 {
                    if input[13] < 0.43141693_f64 {
                        var63 = 0.010596368_f64;
                    } else {
                        var63 = 0.007381258_f64;
                    }
                } else {
                    if input[15] < 33.0_f64 {
                        var63 = 0.005789595_f64;
                    } else {
                        var63 = 0.009602121_f64;
                    }
                }
            } else {
                if input[10] < 0.110275686_f64 {
                    if input[11] < 0.32557118_f64 {
                        var63 = 0.0059158294_f64;
                    } else {
                        var63 = -0.0015695688_f64;
                    }
                } else {
                    if input[35] < 18.283422_f64 {
                        var63 = 0.004745318_f64;
                    } else {
                        var63 = 0.008857845_f64;
                    }
                }
            }
        }
    }
    let var64: f64;
    if input[7] < 128.0_f64 {
        if input[30] < 10.0_f64 {
            if input[8] < 310.0_f64 {
                if input[12] < 0.07342466_f64 {
                    if input[2] < 50.0_f64 {
                        var64 = -0.05817262_f64;
                    } else {
                        var64 = 0.001849014_f64;
                    }
                } else {
                    if input[2] < 94.0_f64 {
                        var64 = 0.0030670636_f64;
                    } else {
                        var64 = 0.00985382_f64;
                    }
                }
            } else {
                if input[11] < 0.19019139_f64 {
                    if input[13] < 0.41753653_f64 {
                        var64 = -0.0063802633_f64;
                    } else {
                        var64 = -0.0401793_f64;
                    }
                } else {
                    if input[8] < 330.0_f64 {
                        var64 = -0.020825109_f64;
                    } else {
                        var64 = 0.002136615_f64;
                    }
                }
            }
        } else {
            if input[29] < 316.0_f64 {
                if input[11] < 0.25804585_f64 {
                    if input[35] < 17.571428_f64 {
                        var64 = 0.0036040004_f64;
                    } else {
                        var64 = 0.0066371816_f64;
                    }
                } else {
                    if input[13] < 0.41893157_f64 {
                        var64 = 0.004569082_f64;
                    } else {
                        var64 = -0.0024519449_f64;
                    }
                }
            } else {
                if input[17] < 1494.0_f64 {
                    if input[30] < 15.0_f64 {
                        var64 = -0.04650442_f64;
                    } else {
                        var64 = -0.006947922_f64;
                    }
                } else {
                    if input[35] < 17.738255_f64 {
                        var64 = -0.009535424_f64;
                    } else {
                        var64 = 0.0029821272_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 18.0_f64 {
            if input[12] < 0.22401847_f64 {
                if input[10] < 0.1558642_f64 {
                    if input[15] < 41.0_f64 {
                        var64 = 0.004023426_f64;
                    } else {
                        var64 = 0.014734044_f64;
                    }
                } else {
                    if input[10] < 0.33581847_f64 {
                        var64 = 0.007265217_f64;
                    } else {
                        var64 = 0.0029404582_f64;
                    }
                }
            } else {
                if input[10] < 0.26643598_f64 {
                    if input[11] < 0.2211939_f64 {
                        var64 = 0.009238169_f64;
                    } else {
                        var64 = 0.0065688016_f64;
                    }
                } else {
                    if input[13] < 0.39510748_f64 {
                        var64 = 0.0045673437_f64;
                    } else {
                        var64 = -0.009004564_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.20704846_f64 {
                if input[10] < 0.29043126_f64 {
                    if input[5] < 423.0_f64 {
                        var64 = 0.009971885_f64;
                    } else {
                        var64 = 0.012207887_f64;
                    }
                } else {
                    if input[6] < 52.0_f64 {
                        var64 = -0.043801453_f64;
                    } else {
                        var64 = 0.00792171_f64;
                    }
                }
            } else {
                if input[15] < 45.0_f64 {
                    if input[13] < 0.39241052_f64 {
                        var64 = 0.00882532_f64;
                    } else {
                        var64 = 0.0059593692_f64;
                    }
                } else {
                    if input[22] < 7.884595_f64 {
                        var64 = 0.008765018_f64;
                    } else {
                        var64 = 0.020713214_f64;
                    }
                }
            }
        }
    }
    let var65: f64;
    if input[15] < 28.0_f64 {
        if input[12] < 0.17261904_f64 {
            if input[29] < 41.0_f64 {
                if input[10] < 0.2820513_f64 {
                    if input[11] < 0.2281106_f64 {
                        var65 = 0.0050942334_f64;
                    } else {
                        var65 = -0.0046351454_f64;
                    }
                } else {
                    if input[11] < 0.163134_f64 {
                        var65 = -0.0018273434_f64;
                    } else {
                        var65 = -0.02197775_f64;
                    }
                }
            } else {
                if input[13] < 0.41323647_f64 {
                    if input[30] < 16.0_f64 {
                        var65 = 0.004024213_f64;
                    } else {
                        var65 = 0.007401877_f64;
                    }
                } else {
                    if input[17] < 2466.0_f64 {
                        var65 = 0.0025714503_f64;
                    } else {
                        var65 = -0.0065406202_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.2875817_f64 {
                if input[30] < 13.0_f64 {
                    if input[13] < 0.4027778_f64 {
                        var65 = 0.0059746993_f64;
                    } else {
                        var65 = 0.0033485317_f64;
                    }
                } else {
                    if input[5] < 660.0_f64 {
                        var65 = 0.0074538747_f64;
                    } else {
                        var65 = -0.023742426_f64;
                    }
                }
            } else {
                if input[1] < 8.978_f64 {
                    if input[29] < 41.0_f64 {
                        var65 = 0.0123597225_f64;
                    } else {
                        var65 = 0.00060855394_f64;
                    }
                } else {
                    if input[12] < 0.19248678_f64 {
                        var65 = 0.0023568757_f64;
                    } else {
                        var65 = -0.020468675_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.1300813_f64 {
            if input[11] < 0.12880678_f64 {
                if input[4] < 4562.0_f64 {
                    if input[11] < 0.11730546_f64 {
                        var65 = -0.010579045_f64;
                    } else {
                        var65 = 0.011485252_f64;
                    }
                } else {
                    if input[2] < 41.0_f64 {
                        var65 = -0.049372006_f64;
                    } else {
                        var65 = -0.011277868_f64;
                    }
                }
            } else {
                if input[10] < 0.14522919_f64 {
                    if input[22] < 5.849868_f64 {
                        var65 = -0.012849392_f64;
                    } else {
                        var65 = 0.004513682_f64;
                    }
                } else {
                    if input[30] < 11.0_f64 {
                        var65 = 0.00062587234_f64;
                    } else {
                        var65 = 0.0058202934_f64;
                    }
                }
            }
        } else {
            if input[15] < 38.0_f64 {
                if input[11] < 0.2256_f64 {
                    if input[10] < 0.2961165_f64 {
                        var65 = 0.008275188_f64;
                    } else {
                        var65 = 0.0051046717_f64;
                    }
                } else {
                    if input[10] < 0.13035715_f64 {
                        var65 = 0.003600175_f64;
                    } else {
                        var65 = 0.0068814144_f64;
                    }
                }
            } else {
                if input[11] < 0.31177828_f64 {
                    if input[25] < 0.006695871_f64 {
                        var65 = 0.010541388_f64;
                    } else {
                        var65 = 0.007784512_f64;
                    }
                } else {
                    if input[30] < 13.0_f64 {
                        var65 = 0.022772372_f64;
                    } else {
                        var65 = 0.0014432652_f64;
                    }
                }
            }
        }
    }
    let var66: f64;
    if input[15] < 30.0_f64 {
        if input[12] < 0.14899713_f64 {
            if input[35] < 17.238165_f64 {
                if input[4] < 12102.0_f64 {
                    if input[12] < 0.07342466_f64 {
                        var66 = -0.020239932_f64;
                    } else {
                        var66 = -0.0012934714_f64;
                    }
                } else {
                    if input[0] < 1785.0_f64 {
                        var66 = -0.04337973_f64;
                    } else {
                        var66 = 0.009308684_f64;
                    }
                }
            } else {
                if input[5] < 79.0_f64 {
                    if input[7] < 54.0_f64 {
                        var66 = 0.00055806705_f64;
                    } else {
                        var66 = -0.0121394545_f64;
                    }
                } else {
                    if input[10] < 0.37548056_f64 {
                        var66 = 0.00399694_f64;
                    } else {
                        var66 = -0.0034755785_f64;
                    }
                }
            }
        } else {
            if input[10] < 0.14970563_f64 {
                if input[24] < 161555.0_f64 {
                    if input[19] < 153.02295_f64 {
                        var66 = 0.003916781_f64;
                    } else {
                        var66 = 0.000010326679_f64;
                    }
                } else {
                    if input[2] < 91.0_f64 {
                        var66 = -0.033884324_f64;
                    } else {
                        var66 = 0.001903718_f64;
                    }
                }
            } else {
                if input[12] < 0.2265861_f64 {
                    if input[19] < 68.88758_f64 {
                        var66 = 0.0027553933_f64;
                    } else {
                        var66 = 0.005530004_f64;
                    }
                } else {
                    if input[10] < 0.25016677_f64 {
                        var66 = 0.007561106_f64;
                    } else {
                        var66 = 0.0036969054_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.10612245_f64 {
            if input[22] < 6.456181_f64 {
                if input[10] < 0.16495806_f64 {
                    if input[6] < 453.0_f64 {
                        var66 = 0.011888946_f64;
                    } else {
                        var66 = -0.0218176_f64;
                    }
                } else {
                    if input[11] < 0.123484015_f64 {
                        var66 = -0.02189464_f64;
                    } else {
                        var66 = 0.0022544393_f64;
                    }
                }
            } else {
                if input[2] < 100.0_f64 {
                    if input[7] < 1327.0_f64 {
                        var66 = 0.0060444972_f64;
                    } else {
                        var66 = 0.018899988_f64;
                    }
                } else {
                    if input[5] < 1085.0_f64 {
                        var66 = -0.056147195_f64;
                    } else {
                        var66 = 0.006285816_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.28242075_f64 {
                if input[15] < 36.0_f64 {
                    if input[13] < 0.27929688_f64 {
                        var66 = -0.0028514029_f64;
                    } else {
                        var66 = 0.0065495046_f64;
                    }
                } else {
                    if input[15] < 44.0_f64 {
                        var66 = 0.007746396_f64;
                    } else {
                        var66 = 0.011275928_f64;
                    }
                }
            } else {
                if input[22] < 4.8675985_f64 {
                    if input[11] < 0.1954638_f64 {
                        var66 = 0.022882042_f64;
                    } else {
                        var66 = -0.015090785_f64;
                    }
                } else {
                    if input[10] < 0.32578397_f64 {
                        var66 = 0.009179383_f64;
                    } else {
                        var66 = -0.023234097_f64;
                    }
                }
            }
        }
    }
    let var67: f64;
    if input[7] < 266.0_f64 {
        if input[30] < 18.0_f64 {
            if input[12] < 0.22083333_f64 {
                if input[5] < 73.0_f64 {
                    if input[20] < 13.659193_f64 {
                        var67 = 0.0014913442_f64;
                    } else {
                        var67 = -0.008405597_f64;
                    }
                } else {
                    if input[11] < 0.10509839_f64 {
                        var67 = -0.0030879162_f64;
                    } else {
                        var67 = 0.004223326_f64;
                    }
                }
            } else {
                if input[11] < 0.21066667_f64 {
                    if input[16] < 26.362997_f64 {
                        var67 = 0.006758816_f64;
                    } else {
                        var67 = 0.0043928726_f64;
                    }
                } else {
                    if input[17] < 1075.0_f64 {
                        var67 = 0.0013088415_f64;
                    } else {
                        var67 = 0.005796619_f64;
                    }
                }
            }
        } else {
            if input[8] < 678.0_f64 {
                if input[35] < 18.95267_f64 {
                    if input[35] < 17.866903_f64 {
                        var67 = 0.0047631655_f64;
                    } else {
                        var67 = 0.0076730894_f64;
                    }
                } else {
                    if input[20] < 14.919574_f64 {
                        var67 = 0.010089791_f64;
                    } else {
                        var67 = 0.0024298772_f64;
                    }
                }
            } else {
                if input[6] < 637.0_f64 {
                    if input[12] < 0.080063626_f64 {
                        var67 = -0.02673818_f64;
                    } else {
                        var67 = -0.00074600073_f64;
                    }
                } else {
                    if input[2] < 8.0_f64 {
                        var67 = -0.010331409_f64;
                    } else {
                        var67 = 0.010165898_f64;
                    }
                }
            }
        }
    } else {
        if input[30] < 10.0_f64 {
            if input[11] < 0.07709251_f64 {
                if input[7] < 395.0_f64 {
                    var67 = -0.053426888_f64;
                } else {
                    if input[16] < 26.685286_f64 {
                        var67 = 0.0079452535_f64;
                    } else {
                        var67 = -0.015064159_f64;
                    }
                }
            } else {
                if input[13] < 0.44163424_f64 {
                    if input[35] < 18.859701_f64 {
                        var67 = 0.0049240175_f64;
                    } else {
                        var67 = -0.000015526648_f64;
                    }
                } else {
                    if input[12] < 0.26436782_f64 {
                        var67 = -0.0019276835_f64;
                    } else {
                        var67 = -0.05622529_f64;
                    }
                }
            }
        } else {
            if input[15] < 45.0_f64 {
                if input[12] < 0.12069428_f64 {
                    if input[35] < 17.109346_f64 {
                        var67 = -0.010235047_f64;
                    } else {
                        var67 = 0.003419817_f64;
                    }
                } else {
                    if input[11] < 0.23570432_f64 {
                        var67 = 0.0069684386_f64;
                    } else {
                        var67 = 0.0055546556_f64;
                    }
                }
            } else {
                if input[4] < 3396.0_f64 {
                    if input[16] < 36.40073_f64 {
                        var67 = -0.0040308926_f64;
                    } else {
                        var67 = 0.018719796_f64;
                    }
                } else {
                    if input[2] < 21.0_f64 {
                        var67 = -0.0018345735_f64;
                    } else {
                        var67 = 0.011264867_f64;
                    }
                }
            }
        }
    }
    let var68: f64;
    if input[15] < 28.0_f64 {
        if input[11] < 0.25804585_f64 {
            if input[10] < 0.26643598_f64 {
                if input[13] < 0.40008345_f64 {
                    if input[11] < 0.20651747_f64 {
                        var68 = 0.006273787_f64;
                    } else {
                        var68 = 0.0044433773_f64;
                    }
                } else {
                    if input[13] < 0.46285716_f64 {
                        var68 = 0.0033948843_f64;
                    } else {
                        var68 = -0.007424086_f64;
                    }
                }
            } else {
                if input[20] < 11.424528_f64 {
                    if input[6] < 157.0_f64 {
                        var68 = -0.000109740104_f64;
                    } else {
                        var68 = -0.048777733_f64;
                    }
                } else {
                    if input[35] < 17.74646_f64 {
                        var68 = -0.0000213474_f64;
                    } else {
                        var68 = 0.003830586_f64;
                    }
                }
            }
        } else {
            if input[24] < 111809.0_f64 {
                if input[11] < 0.30880615_f64 {
                    if input[22] < 5.5425453_f64 {
                        var68 = 0.0025630686_f64;
                    } else {
                        var68 = -0.003432742_f64;
                    }
                } else {
                    if input[30] < 10.0_f64 {
                        var68 = -0.0075602396_f64;
                    } else {
                        var68 = -0.0004865305_f64;
                    }
                }
            } else {
                if input[11] < 0.38214287_f64 {
                    if input[22] < 4.7004967_f64 {
                        var68 = 0.0030263138_f64;
                    } else {
                        var68 = 0.0097455345_f64;
                    }
                } else {
                    var68 = -0.04133993_f64;
                }
            }
        }
    } else {
        if input[10] < 0.35_f64 {
            if input[11] < 0.2256_f64 {
                if input[35] < 17.718607_f64 {
                    if input[12] < 0.14978448_f64 {
                        var68 = 0.0015283304_f64;
                    } else {
                        var68 = 0.0052354196_f64;
                    }
                } else {
                    if input[15] < 33.0_f64 {
                        var68 = 0.0059716995_f64;
                    } else {
                        var68 = 0.007446134_f64;
                    }
                }
            } else {
                if input[15] < 38.0_f64 {
                    if input[11] < 0.36167213_f64 {
                        var68 = 0.0045528295_f64;
                    } else {
                        var68 = -0.0024802925_f64;
                    }
                } else {
                    if input[10] < 0.30929792_f64 {
                        var68 = 0.007096006_f64;
                    } else {
                        var68 = -0.0060857083_f64;
                    }
                }
            }
        } else {
            if input[30] < 10.0_f64 {
                if input[22] < 5.3528438_f64 {
                    if input[15] < 29.0_f64 {
                        var68 = -0.010677326_f64;
                    } else {
                        var68 = -0.058113407_f64;
                    }
                } else {
                    if input[22] < 5.5963655_f64 {
                        var68 = 0.017144343_f64;
                    } else {
                        var68 = -0.010515097_f64;
                    }
                }
            } else {
                if input[12] < 0.19354838_f64 {
                    if input[3] < 6346.6816_f64 {
                        var68 = 0.0025877429_f64;
                    } else {
                        var68 = -0.022477375_f64;
                    }
                } else {
                    if input[12] < 0.19774719_f64 {
                        var68 = -0.032471072_f64;
                    } else {
                        var68 = -0.004259547_f64;
                    }
                }
            }
        }
    }
    let var69: f64;
    if input[30] < 11.0_f64 {
        if input[10] < 0.3225058_f64 {
            if input[13] < 0.39285713_f64 {
                if input[35] < 18.712122_f64 {
                    if input[7] < 66.0_f64 {
                        var69 = 0.0011870317_f64;
                    } else {
                        var69 = 0.0051575084_f64;
                    }
                } else {
                    if input[12] < 0.32160804_f64 {
                        var69 = 0.001936151_f64;
                    } else {
                        var69 = 0.008011874_f64;
                    }
                }
            } else {
                if input[15] < 28.0_f64 {
                    if input[24] < 161555.0_f64 {
                        var69 = 0.0008761187_f64;
                    } else {
                        var69 = -0.016361468_f64;
                    }
                } else {
                    if input[35] < 17.718607_f64 {
                        var69 = 0.0010988081_f64;
                    } else {
                        var69 = 0.0065276786_f64;
                    }
                }
            }
        } else {
            if input[22] < 5.3528438_f64 {
                if input[20] < 16.45514_f64 {
                    if input[19] < 142.5912_f64 {
                        var69 = -0.004241672_f64;
                    } else {
                        var69 = 0.019597715_f64;
                    }
                } else {
                    if input[7] < 1963.0_f64 {
                        var69 = -0.02991722_f64;
                    } else {
                        var69 = 0.020673996_f64;
                    }
                }
            } else {
                if input[20] < 15.56671_f64 {
                    if input[7] < 49.0_f64 {
                        var69 = -0.008552114_f64;
                    } else {
                        var69 = 0.026248395_f64;
                    }
                } else {
                    if input[11] < 0.13636364_f64 {
                        var69 = -0.009874691_f64;
                    } else {
                        var69 = 0.008380364_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 181.0_f64 {
            if input[13] < 0.42833108_f64 {
                if input[11] < 0.25368324_f64 {
                    if input[10] < 0.29043126_f64 {
                        var69 = 0.004810992_f64;
                    } else {
                        var69 = 0.0027490864_f64;
                    }
                } else {
                    if input[35] < 18.897121_f64 {
                        var69 = 0.0038834375_f64;
                    } else {
                        var69 = 0.000437871_f64;
                    }
                }
            } else {
                if input[35] < 17.718607_f64 {
                    if input[10] < 0.26150122_f64 {
                        var69 = 0.0022692888_f64;
                    } else {
                        var69 = -0.004427909_f64;
                    }
                } else {
                    if input[0] < 1381.0_f64 {
                        var69 = -0.0062841587_f64;
                    } else {
                        var69 = -0.04205888_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.33045977_f64 {
                if input[7] < 703.0_f64 {
                    if input[13] < 0.405954_f64 {
                        var69 = 0.005407587_f64;
                    } else {
                        var69 = 0.0038425424_f64;
                    }
                } else {
                    if input[22] < 4.322658_f64 {
                        var69 = -0.010180014_f64;
                    } else {
                        var69 = 0.006594941_f64;
                    }
                }
            } else {
                if input[25] < 0.00068372575_f64 {
                    if input[11] < 0.36167213_f64 {
                        var69 = 0.00792729_f64;
                    } else {
                        var69 = 0.024115345_f64;
                    }
                } else {
                    if input[8] < 3888.0_f64 {
                        var69 = 0.0005835902_f64;
                    } else {
                        var69 = -0.048101667_f64;
                    }
                }
            }
        }
    }
    let var70: f64;
    if input[30] < 18.0_f64 {
        if input[12] < 0.16783217_f64 {
            if input[12] < 0.07342466_f64 {
                if input[24] < 42603.0_f64 {
                    if input[11] < 0.29946524_f64 {
                        var70 = -0.0020087908_f64;
                    } else {
                        var70 = -0.026143743_f64;
                    }
                } else {
                    if input[11] < 0.17094018_f64 {
                        var70 = -0.020166742_f64;
                    } else {
                        var70 = 0.00030102415_f64;
                    }
                }
            } else {
                if input[10] < 0.1558642_f64 {
                    if input[12] < 0.08512975_f64 {
                        var70 = -0.02664787_f64;
                    } else {
                        var70 = -0.0005243214_f64;
                    }
                } else {
                    if input[6] < 164.0_f64 {
                        var70 = 0.0017456139_f64;
                    } else {
                        var70 = 0.0035880327_f64;
                    }
                }
            }
        } else {
            if input[5] < 115.0_f64 {
                if input[11] < 0.2875817_f64 {
                    if input[13] < 0.4027778_f64 {
                        var70 = 0.0034855746_f64;
                    } else {
                        var70 = 0.0009165855_f64;
                    }
                } else {
                    if input[16] < 21.584862_f64 {
                        var70 = 0.010051294_f64;
                    } else {
                        var70 = -0.00447433_f64;
                    }
                }
            } else {
                if input[19] < 60.19968_f64 {
                    if input[7] < 89.0_f64 {
                        var70 = -0.05739085_f64;
                    } else {
                        var70 = -0.0038842328_f64;
                    }
                } else {
                    if input[10] < 0.24941905_f64 {
                        var70 = 0.0048286445_f64;
                    } else {
                        var70 = 0.003152379_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.17879274_f64 {
            if input[4] < 6556.0_f64 {
                if input[11] < 0.36167213_f64 {
                    if input[15] < 40.0_f64 {
                        var70 = 0.004904132_f64;
                    } else {
                        var70 = 0.009834376_f64;
                    }
                } else {
                    if input[1] < 3.8481233_f64 {
                        var70 = 0.010394783_f64;
                    } else {
                        var70 = -0.016361466_f64;
                    }
                }
            } else {
                if input[24] < 95499.0_f64 {
                    if input[13] < 0.3211404_f64 {
                        var70 = 0.011644357_f64;
                    } else {
                        var70 = -0.00023546659_f64;
                    }
                } else {
                    if input[4] < 6684.0_f64 {
                        var70 = -0.036673333_f64;
                    } else {
                        var70 = 0.0051091793_f64;
                    }
                }
            }
        } else {
            if input[16] < 44.547756_f64 {
                if input[13] < 0.3253012_f64 {
                    if input[13] < 0.32417583_f64 {
                        var70 = 0.003999688_f64;
                    } else {
                        var70 = -0.01185733_f64;
                    }
                } else {
                    if input[13] < 0.3802817_f64 {
                        var70 = 0.0071723773_f64;
                    } else {
                        var70 = 0.0053728404_f64;
                    }
                }
            } else {
                if input[10] < 0.26498422_f64 {
                    if input[10] < 0.13652053_f64 {
                        var70 = 0.006897499_f64;
                    } else {
                        var70 = 0.019148646_f64;
                    }
                } else {
                    if input[10] < 0.28658536_f64 {
                        var70 = -0.008055585_f64;
                    } else {
                        var70 = 0.013470413_f64;
                    }
                }
            }
        }
    }
    let var71: f64;
    if input[30] < 11.0_f64 {
        if input[11] < 0.0931677_f64 {
            if input[15] < 36.0_f64 {
                if input[16] < 26.362997_f64 {
                    if input[15] < 25.0_f64 {
                        var71 = -0.009913507_f64;
                    } else {
                        var71 = 0.0092126895_f64;
                    }
                } else {
                    if input[26] < 9.457787_f64 {
                        var71 = 0.008769663_f64;
                    } else {
                        var71 = -0.01790134_f64;
                    }
                }
            } else {
                var71 = 0.01882587_f64;
            }
        } else {
            if input[12] < 0.13118812_f64 {
                if input[1] < 5.792373_f64 {
                    if input[6] < 127.0_f64 {
                        var71 = -0.00340942_f64;
                    } else {
                        var71 = 0.00541992_f64;
                    }
                } else {
                    if input[22] < 6.3436112_f64 {
                        var71 = -0.0033528612_f64;
                    } else {
                        var71 = 0.018870166_f64;
                    }
                }
            } else {
                if input[11] < 0.38214287_f64 {
                    if input[13] < 0.33223847_f64 {
                        var71 = 0.00064164307_f64;
                    } else {
                        var71 = 0.003001103_f64;
                    }
                } else {
                    if input[3] < 3680.3635_f64 {
                        var71 = -0.0050222743_f64;
                    } else {
                        var71 = -0.05242153_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.24329026_f64 {
            if input[10] < 0.10747664_f64 {
                if input[26] < 170.85095_f64 {
                    if input[1] < 10.697594_f64 {
                        var71 = -0.0017809138_f64;
                    } else {
                        var71 = 0.013527818_f64;
                    }
                } else {
                    if input[30] < 13.0_f64 {
                        var71 = -0.037319988_f64;
                    } else {
                        var71 = -0.009519747_f64;
                    }
                }
            } else {
                if input[7] < 207.0_f64 {
                    if input[6] < 503.0_f64 {
                        var71 = 0.0031228364_f64;
                    } else {
                        var71 = -0.004189882_f64;
                    }
                } else {
                    if input[10] < 0.37548056_f64 {
                        var71 = 0.004275712_f64;
                    } else {
                        var71 = -0.0033588184_f64;
                    }
                }
            }
        } else {
            if input[13] < 0.3153786_f64 {
                if input[22] < 4.433995_f64 {
                    if input[35] < 20.16387_f64 {
                        var71 = -0.004765188_f64;
                    } else {
                        var71 = -0.044630446_f64;
                    }
                } else {
                    if input[1] < 11.289093_f64 {
                        var71 = 0.002905527_f64;
                    } else {
                        var71 = -0.014546931_f64;
                    }
                }
            } else {
                if input[11] < 0.08375_f64 {
                    if input[8] < 447.0_f64 {
                        var71 = -0.008366334_f64;
                    } else {
                        var71 = 0.0026820207_f64;
                    }
                } else {
                    if input[29] < 1115.0_f64 {
                        var71 = 0.005379514_f64;
                    } else {
                        var71 = 0.0101906555_f64;
                    }
                }
            }
        }
    }
    let var72: f64;
    if input[30] < 18.0_f64 {
        if input[12] < 0.23003472_f64 {
            if input[10] < 0.35_f64 {
                if input[5] < 73.0_f64 {
                    if input[6] < 104.0_f64 {
                        var72 = 0.0008579286_f64;
                    } else {
                        var72 = -0.0049218712_f64;
                    }
                } else {
                    if input[13] < 0.4293405_f64 {
                        var72 = 0.0030210789_f64;
                    } else {
                        var72 = 0.00077512796_f64;
                    }
                }
            } else {
                if input[24] < 135403.0_f64 {
                    if input[12] < 0.18401015_f64 {
                        var72 = 0.00017517035_f64;
                    } else {
                        var72 = -0.008171552_f64;
                    }
                } else {
                    if input[11] < 0.17475729_f64 {
                        var72 = -0.007131041_f64;
                    } else {
                        var72 = -0.051448323_f64;
                    }
                }
            }
        } else {
            if input[10] < 0.26741394_f64 {
                if input[11] < 0.21859904_f64 {
                    if input[0] < 5632.0_f64 {
                        var72 = 0.004336722_f64;
                    } else {
                        var72 = 0.008908881_f64;
                    }
                } else {
                    if input[7] < 347.0_f64 {
                        var72 = 0.0006391951_f64;
                    } else {
                        var72 = 0.0038077594_f64;
                    }
                }
            } else {
                if input[26] < 16.026628_f64 {
                    if input[10] < 0.2710911_f64 {
                        var72 = -0.047006752_f64;
                    } else {
                        var72 = -0.0060420656_f64;
                    }
                } else {
                    if input[35] < 18.5562_f64 {
                        var72 = 0.0044792825_f64;
                    } else {
                        var72 = -0.00088449474_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.2877698_f64 {
            if input[13] < 0.31913877_f64 {
                if input[24] < 67647.0_f64 {
                    if input[26] < 60.927094_f64 {
                        var72 = 0.00058049447_f64;
                    } else {
                        var72 = -0.017299924_f64;
                    }
                } else {
                    if input[4] < 8017.0_f64 {
                        var72 = 0.007609802_f64;
                    } else {
                        var72 = 0.00013159087_f64;
                    }
                }
            } else {
                if input[13] < 0.4041451_f64 {
                    if input[10] < 0.15400203_f64 {
                        var72 = 0.0022144779_f64;
                    } else {
                        var72 = 0.005250659_f64;
                    }
                } else {
                    if input[35] < 18.098145_f64 {
                        var72 = 0.0036748443_f64;
                    } else {
                        var72 = -0.0064065405_f64;
                    }
                }
            }
        } else {
            if input[3] < 5498.9546_f64 {
                if input[20] < 23.430506_f64 {
                    if input[26] < 197.98845_f64 {
                        var72 = 0.007302066_f64;
                    } else {
                        var72 = -0.0065905997_f64;
                    }
                } else {
                    if input[4] < 1621.0_f64 {
                        var72 = 0.026381522_f64;
                    } else {
                        var72 = 0.0114342645_f64;
                    }
                }
            } else {
                if input[24] < 130576.0_f64 {
                    if input[16] < 37.356094_f64 {
                        var72 = -0.001923224_f64;
                    } else {
                        var72 = -0.024295744_f64;
                    }
                } else {
                    if input[1] < 4.5955763_f64 {
                        var72 = -0.008249783_f64;
                    } else {
                        var72 = 0.011024138_f64;
                    }
                }
            }
        }
    }
    let var73: f64;
    if input[30] < 12.0_f64 {
        if input[12] < 0.07342466_f64 {
            if input[35] < 18.515_f64 {
                if input[35] < 18.03752_f64 {
                    if input[10] < 0.33581847_f64 {
                        var73 = -0.0019282198_f64;
                    } else {
                        var73 = -0.023212707_f64;
                    }
                } else {
                    if input[3] < 4790.864_f64 {
                        var73 = -0.03313643_f64;
                    } else {
                        var73 = 0.0053511197_f64;
                    }
                }
            } else {
                if input[13] < 0.32922128_f64 {
                    if input[1] < 9.172678_f64 {
                        var73 = -0.0221041_f64;
                    } else {
                        var73 = 0.008613905_f64;
                    }
                } else {
                    if input[11] < 0.3042328_f64 {
                        var73 = 0.022771342_f64;
                    } else {
                        var73 = 0.0040694713_f64;
                    }
                }
            }
        } else {
            if input[15] < 24.0_f64 {
                if input[11] < 0.102564104_f64 {
                    if input[5] < 299.0_f64 {
                        var73 = -0.0065557547_f64;
                    } else {
                        var73 = -0.039400037_f64;
                    }
                } else {
                    if input[16] < 28.171534_f64 {
                        var73 = 0.0014707132_f64;
                    } else {
                        var73 = -0.04289795_f64;
                    }
                }
            } else {
                if input[16] < 25.496319_f64 {
                    if input[29] < 104.0_f64 {
                        var73 = 0.00043356558_f64;
                    } else {
                        var73 = 0.0047113476_f64;
                    }
                } else {
                    if input[19] < 111.80336_f64 {
                        var73 = -0.0015206035_f64;
                    } else {
                        var73 = 0.0023848899_f64;
                    }
                }
            }
        }
    } else {
        if input[10] < 0.35_f64 {
            if input[7] < 307.0_f64 {
                if input[11] < 0.34256172_f64 {
                    if input[12] < 0.09598741_f64 {
                        var73 = -0.00056755514_f64;
                    } else {
                        var73 = 0.0030901895_f64;
                    }
                } else {
                    if input[7] < 254.0_f64 {
                        var73 = -0.00044993762_f64;
                    } else {
                        var73 = -0.016420312_f64;
                    }
                }
            } else {
                if input[13] < 0.41821945_f64 {
                    if input[10] < 0.15306123_f64 {
                        var73 = 0.0028472026_f64;
                    } else {
                        var73 = 0.004603066_f64;
                    }
                } else {
                    if input[16] < 26.362997_f64 {
                        var73 = 0.0100373095_f64;
                    } else {
                        var73 = 0.0021150375_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.19354838_f64 {
                if input[30] < 15.0_f64 {
                    if input[1] < 8.463247_f64 {
                        var73 = -0.006653757_f64;
                    } else {
                        var73 = 0.00568417_f64;
                    }
                } else {
                    if input[4] < 3739.0_f64 {
                        var73 = 0.0062737702_f64;
                    } else {
                        var73 = -0.00031987205_f64;
                    }
                }
            } else {
                if input[2] < 35.0_f64 {
                    if input[3] < 1285.2632_f64 {
                        var73 = -0.013934525_f64;
                    } else {
                        var73 = -0.06515259_f64;
                    }
                } else {
                    if input[12] < 0.19774719_f64 {
                        var73 = -0.019020606_f64;
                    } else {
                        var73 = 0.002699657_f64;
                    }
                }
            }
        }
    }
    let var74: f64;
    if input[30] < 10.0_f64 {
        if input[13] < 0.41893157_f64 {
            if input[10] < 0.3394348_f64 {
                if input[11] < 0.3019608_f64 {
                    if input[25] < 1.1988763_f64 {
                        var74 = 0.0020284366_f64;
                    } else {
                        var74 = -0.0031537642_f64;
                    }
                } else {
                    if input[2] < 89.0_f64 {
                        var74 = -0.0052417438_f64;
                    } else {
                        var74 = 0.011367622_f64;
                    }
                }
            } else {
                if input[16] < 28.224092_f64 {
                    if input[8] < 447.0_f64 {
                        var74 = -0.0057538743_f64;
                    } else {
                        var74 = 0.018394617_f64;
                    }
                } else {
                    if input[15] < 35.0_f64 {
                        var74 = -0.030197129_f64;
                    } else {
                        var74 = 0.0049304445_f64;
                    }
                }
            }
        } else {
            if input[1] < 2.5158632_f64 {
                if input[10] < 0.13926017_f64 {
                    var74 = 0.02484244_f64;
                } else {
                    if input[15] < 20.0_f64 {
                        var74 = -0.0030259804_f64;
                    } else {
                        var74 = 0.011004309_f64;
                    }
                }
            } else {
                if input[1] < 4.065793_f64 {
                    if input[1] < 3.8153753_f64 {
                        var74 = -0.0048129056_f64;
                    } else {
                        var74 = -0.027209789_f64;
                    }
                } else {
                    if input[12] < 0.23137744_f64 {
                        var74 = 0.00012672566_f64;
                    } else {
                        var74 = -0.009199395_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.16605166_f64 {
            if input[22] < 6.613095_f64 {
                if input[10] < 0.14970563_f64 {
                    if input[11] < 0.28440368_f64 {
                        var74 = -0.013488501_f64;
                    } else {
                        var74 = -0.00086271606_f64;
                    }
                } else {
                    if input[11] < 0.14437367_f64 {
                        var74 = -0.0017282831_f64;
                    } else {
                        var74 = 0.0020110917_f64;
                    }
                }
            } else {
                if input[35] < 17.201937_f64 {
                    if input[15] < 40.0_f64 {
                        var74 = -0.009953082_f64;
                    } else {
                        var74 = 0.003994696_f64;
                    }
                } else {
                    if input[15] < 45.0_f64 {
                        var74 = 0.0038414102_f64;
                    } else {
                        var74 = 0.009009435_f64;
                    }
                }
            }
        } else {
            if input[19] < 184.59396_f64 {
                if input[35] < 19.862576_f64 {
                    if input[13] < 0.45728898_f64 {
                        var74 = 0.0029465265_f64;
                    } else {
                        var74 = -0.0037011083_f64;
                    }
                } else {
                    if input[2] < 18.0_f64 {
                        var74 = -0.014532762_f64;
                    } else {
                        var74 = -0.00070361426_f64;
                    }
                }
            } else {
                if input[22] < 4.209721_f64 {
                    if input[6] < 1325.0_f64 {
                        var74 = -0.018412638_f64;
                    } else {
                        var74 = 0.0028610062_f64;
                    }
                } else {
                    if input[10] < 0.07663783_f64 {
                        var74 = -0.004608422_f64;
                    } else {
                        var74 = 0.004129546_f64;
                    }
                }
            }
        }
    }
    let var75: f64;
    if input[30] < 18.0_f64 {
        if input[12] < 0.22401847_f64 {
            if input[30] < 10.0_f64 {
                if input[2] < 95.0_f64 {
                    if input[35] < 20.16387_f64 {
                        var75 = -0.0001311953_f64;
                    } else {
                        var75 = -0.035060637_f64;
                    }
                } else {
                    if input[5] < 69.0_f64 {
                        var75 = -0.0123699475_f64;
                    } else {
                        var75 = 0.0077760927_f64;
                    }
                }
            } else {
                if input[10] < 0.1558642_f64 {
                    if input[12] < 0.08512975_f64 {
                        var75 = -0.020371446_f64;
                    } else {
                        var75 = 0.00049283355_f64;
                    }
                } else {
                    if input[11] < 0.124938026_f64 {
                        var75 = -0.00029395265_f64;
                    } else {
                        var75 = 0.0022636931_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.08375_f64 {
                if input[1] < 12.150158_f64 {
                    if input[35] < 19.19658_f64 {
                        var75 = -0.001639241_f64;
                    } else {
                        var75 = -0.02469328_f64;
                    }
                } else {
                    var75 = -0.03075455_f64;
                }
            } else {
                if input[10] < 0.110275686_f64 {
                    if input[22] < 5.0935316_f64 {
                        var75 = -0.00445497_f64;
                    } else {
                        var75 = 0.0018302726_f64;
                    }
                } else {
                    if input[25] < 0.0037467263_f64 {
                        var75 = 0.0052453047_f64;
                    } else {
                        var75 = 0.0028803565_f64;
                    }
                }
            }
        }
    } else {
        if input[20] < 25.892977_f64 {
            if input[11] < 0.20704846_f64 {
                if input[10] < 0.2710911_f64 {
                    if input[5] < 75.0_f64 {
                        var75 = -0.005415006_f64;
                    } else {
                        var75 = 0.004693607_f64;
                    }
                } else {
                    if input[2] < 99.0_f64 {
                        var75 = 0.0022426767_f64;
                    } else {
                        var75 = 0.013079642_f64;
                    }
                }
            } else {
                if input[35] < 17.866903_f64 {
                    if input[11] < 0.21112256_f64 {
                        var75 = -0.014671259_f64;
                    } else {
                        var75 = 0.00084786705_f64;
                    }
                } else {
                    if input[1] < 10.076003_f64 {
                        var75 = 0.0033361316_f64;
                    } else {
                        var75 = -0.0014601279_f64;
                    }
                }
            }
        } else {
            if input[4] < 5954.0_f64 {
                if input[35] < 18.521347_f64 {
                    if input[6] < 1831.0_f64 {
                        var75 = 0.016463524_f64;
                    } else {
                        var75 = 0.0008755741_f64;
                    }
                } else {
                    if input[10] < 0.20269966_f64 {
                        var75 = 0.028780445_f64;
                    } else {
                        var75 = 0.0128016_f64;
                    }
                }
            } else {
                if input[24] < 90351.0_f64 {
                    if input[15] < 46.0_f64 {
                        var75 = -0.022591598_f64;
                    } else {
                        var75 = -0.000326024_f64;
                    }
                } else {
                    if input[3] < 5349.4287_f64 {
                        var75 = 0.011374279_f64;
                    } else {
                        var75 = -0.0038702793_f64;
                    }
                }
            }
        }
    }
    let var76: f64;
    if input[30] < 17.0_f64 {
        if input[3] < 81.210526_f64 {
            if input[22] < 4.8675985_f64 {
                if input[19] < 134.5988_f64 {
                    if input[8] < 316.0_f64 {
                        var76 = 0.0013677995_f64;
                    } else {
                        var76 = 0.010900996_f64;
                    }
                } else {
                    if input[6] < 213.0_f64 {
                        var76 = -0.045487653_f64;
                    } else {
                        var76 = -0.010787174_f64;
                    }
                }
            } else {
                if input[35] < 18.364511_f64 {
                    if input[29] < 335.0_f64 {
                        var76 = 0.003220111_f64;
                    } else {
                        var76 = 0.017082322_f64;
                    }
                } else {
                    if input[19] < 110.231415_f64 {
                        var76 = 0.015835987_f64;
                    } else {
                        var76 = 0.007209744_f64;
                    }
                }
            }
        } else {
            if input[24] < 3996.0_f64 {
                if input[4] < 236.0_f64 {
                    if input[24] < 2467.0_f64 {
                        var76 = -0.025371686_f64;
                    } else {
                        var76 = -0.00008151794_f64;
                    }
                } else {
                    if input[2] < 5.0_f64 {
                        var76 = -0.03256696_f64;
                    } else {
                        var76 = -0.0076423693_f64;
                    }
                }
            } else {
                if input[15] < 26.0_f64 {
                    if input[10] < 0.15673469_f64 {
                        var76 = -0.0011128223_f64;
                    } else {
                        var76 = 0.0014465664_f64;
                    }
                } else {
                    if input[13] < 0.2934363_f64 {
                        var76 = -0.0017912565_f64;
                    } else {
                        var76 = 0.0022885732_f64;
                    }
                }
            }
        }
    } else {
        if input[7] < 1803.0_f64 {
            if input[10] < 0.2961165_f64 {
                if input[13] < 0.40784603_f64 {
                    if input[11] < 0.31177828_f64 {
                        var76 = 0.0035375336_f64;
                    } else {
                        var76 = 0.000039442235_f64;
                    }
                } else {
                    if input[11] < 0.2053942_f64 {
                        var76 = 0.00295621_f64;
                    } else {
                        var76 = -0.0002506637_f64;
                    }
                }
            } else {
                if input[35] < 19.480465_f64 {
                    if input[3] < 758.7619_f64 {
                        var76 = -0.0027630306_f64;
                    } else {
                        var76 = 0.002291697_f64;
                    }
                } else {
                    if input[7] < 765.0_f64 {
                        var76 = -0.0052682674_f64;
                    } else {
                        var76 = -0.026005426_f64;
                    }
                }
            }
        } else {
            if input[13] < 0.34612104_f64 {
                if input[1] < 10.076003_f64 {
                    if input[35] < 18.976562_f64 {
                        var76 = 0.018495899_f64;
                    } else {
                        var76 = 0.008680179_f64;
                    }
                } else {
                    var76 = -0.021492723_f64;
                }
            } else {
                if input[35] < 18.635206_f64 {
                    if input[10] < 0.21333334_f64 {
                        var76 = 0.00790676_f64;
                    } else {
                        var76 = 0.0020999124_f64;
                    }
                } else {
                    if input[13] < 0.36949152_f64 {
                        var76 = -0.0053523458_f64;
                    } else {
                        var76 = -0.053588778_f64;
                    }
                }
            }
        }
    }
    let var77: f64;
    if input[15] < 34.0_f64 {
        if input[12] < 0.14516129_f64 {
            if input[11] < 0.36167213_f64 {
                if input[11] < 0.13968255_f64 {
                    if input[30] < 12.0_f64 {
                        var77 = 0.001047751_f64;
                    } else {
                        var77 = -0.008298209_f64;
                    }
                } else {
                    if input[19] < 50.294167_f64 {
                        var77 = -0.0062666624_f64;
                    } else {
                        var77 = 0.0010101008_f64;
                    }
                }
            } else {
                if input[13] < 0.3897243_f64 {
                    if input[0] < 753.0_f64 {
                        var77 = -0.013421719_f64;
                    } else {
                        var77 = 0.00080770784_f64;
                    }
                } else {
                    if input[16] < 25.715717_f64 {
                        var77 = -0.00069470395_f64;
                    } else {
                        var77 = -0.04159322_f64;
                    }
                }
            }
        } else {
            if input[5] < 1403.0_f64 {
                if input[35] < 19.862576_f64 {
                    if input[13] < 0.46285716_f64 {
                        var77 = 0.0020709939_f64;
                    } else {
                        var77 = -0.0049970723_f64;
                    }
                } else {
                    if input[26] < 21.093458_f64 {
                        var77 = -0.011220436_f64;
                    } else {
                        var77 = -0.00079594814_f64;
                    }
                }
            } else {
                if input[0] < 5872.0_f64 {
                    if input[13] < 0.39966834_f64 {
                        var77 = -0.016368765_f64;
                    } else {
                        var77 = -0.05810801_f64;
                    }
                } else {
                    if input[20] < 21.173801_f64 {
                        var77 = 0.0006330295_f64;
                    } else {
                        var77 = -0.028832857_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.080063626_f64 {
            if input[22] < 5.8051906_f64 {
                if input[11] < 0.16016074_f64 {
                    var77 = 0.02277208_f64;
                } else {
                    if input[13] < 0.43141693_f64 {
                        var77 = -0.037814163_f64;
                    } else {
                        var77 = 0.007463912_f64;
                    }
                }
            } else {
                if input[4] < 2734.0_f64 {
                    if input[30] < 17.0_f64 {
                        var77 = -0.031781234_f64;
                    } else {
                        var77 = -0.0040240264_f64;
                    }
                } else {
                    if input[3] < 5573.3184_f64 {
                        var77 = 0.004737937_f64;
                    } else {
                        var77 = -0.01729779_f64;
                    }
                }
            }
        } else {
            if input[4] < 764.0_f64 {
                if input[13] < 0.3153786_f64 {
                    if input[0] < 4796.0_f64 {
                        var77 = -0.00095620705_f64;
                    } else {
                        var77 = -0.04809616_f64;
                    }
                } else {
                    if input[7] < 1212.0_f64 {
                        var77 = 0.005813266_f64;
                    } else {
                        var77 = 0.019247556_f64;
                    }
                }
            } else {
                if input[24] < 9736.0_f64 {
                    if input[15] < 38.0_f64 {
                        var77 = -0.05696177_f64;
                    } else {
                        var77 = -0.015370751_f64;
                    }
                } else {
                    if input[5] < 309.0_f64 {
                        var77 = 0.0012505017_f64;
                    } else {
                        var77 = 0.0030209397_f64;
                    }
                }
            }
        }
    }
    let var78: f64;
    if input[30] < 10.0_f64 {
        if input[11] < 0.102564104_f64 {
            if input[4] < 10674.0_f64 {
                if input[2] < 56.0_f64 {
                    if input[4] < 5595.0_f64 {
                        var78 = -0.00431738_f64;
                    } else {
                        var78 = -0.033471446_f64;
                    }
                } else {
                    if input[12] < 0.14594595_f64 {
                        var78 = -0.020753125_f64;
                    } else {
                        var78 = 0.005482406_f64;
                    }
                }
            } else {
                if input[12] < 0.19178082_f64 {
                    var78 = 0.007936166_f64;
                } else {
                    if input[3] < 6042.5454_f64 {
                        var78 = -0.015199274_f64;
                    } else {
                        var78 = -0.046382762_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.22147302_f64 {
                if input[2] < 95.0_f64 {
                    if input[2] < 56.0_f64 {
                        var78 = 0.0006523758_f64;
                    } else {
                        var78 = -0.0023254778_f64;
                    }
                } else {
                    if input[12] < 0.098779134_f64 {
                        var78 = -0.026291057_f64;
                    } else {
                        var78 = 0.005944812_f64;
                    }
                }
            } else {
                if input[13] < 0.41955444_f64 {
                    if input[35] < 18.683113_f64 {
                        var78 = 0.004083522_f64;
                    } else {
                        var78 = -0.0000868588_f64;
                    }
                } else {
                    if input[10] < 0.11335337_f64 {
                        var78 = -0.022027394_f64;
                    } else {
                        var78 = -0.0013642926_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.24329026_f64 {
            if input[0] < 746.0_f64 {
                if input[6] < 203.0_f64 {
                    if input[10] < 0.18523775_f64 {
                        var78 = -0.0008347514_f64;
                    } else {
                        var78 = 0.0013836836_f64;
                    }
                } else {
                    if input[22] < 6.7334175_f64 {
                        var78 = -0.004314851_f64;
                    } else {
                        var78 = -0.030853933_f64;
                    }
                }
            } else {
                if input[13] < 0.39444613_f64 {
                    if input[35] < 19.059431_f64 {
                        var78 = 0.0025702105_f64;
                    } else {
                        var78 = 0.0008718581_f64;
                    }
                } else {
                    if input[12] < 0.17261904_f64 {
                        var78 = 0.00032017718_f64;
                    } else {
                        var78 = 0.0020509604_f64;
                    }
                }
            }
        } else {
            if input[10] < 0.2777778_f64 {
                if input[25] < 0.00030379987_f64 {
                    if input[10] < 0.24136178_f64 {
                        var78 = 0.008794479_f64;
                    } else {
                        var78 = 0.023648446_f64;
                    }
                } else {
                    if input[35] < 19.862576_f64 {
                        var78 = 0.0029406268_f64;
                    } else {
                        var78 = -0.002865089_f64;
                    }
                }
            } else {
                if input[10] < 0.28091604_f64 {
                    if input[8] < 372.0_f64 {
                        var78 = -0.002016737_f64;
                    } else {
                        var78 = -0.02205195_f64;
                    }
                } else {
                    if input[22] < 5.1604013_f64 {
                        var78 = 0.0047443504_f64;
                    } else {
                        var78 = -0.003320902_f64;
                    }
                }
            }
        }
    }
    let var79: f64;
    if input[30] < 18.0_f64 {
        if input[10] < 0.31991714_f64 {
            if input[3] < 81.210526_f64 {
                if input[6] < 119.0_f64 {
                    if input[6] < 112.0_f64 {
                        var79 = 0.0028724957_f64;
                    } else {
                        var79 = -0.019500196_f64;
                    }
                } else {
                    if input[25] < 0.0023812808_f64 {
                        var79 = 0.0052461396_f64;
                    } else {
                        var79 = 0.011737305_f64;
                    }
                }
            } else {
                if input[11] < 0.24369748_f64 {
                    if input[35] < 17.598156_f64 {
                        var79 = 0.00025601842_f64;
                    } else {
                        var79 = 0.0019304457_f64;
                    }
                } else {
                    if input[24] < 3235.0_f64 {
                        var79 = -0.021114394_f64;
                    } else {
                        var79 = 0.00069649046_f64;
                    }
                }
            }
        } else {
            if input[2] < 6.0_f64 {
                if input[11] < 0.18209212_f64 {
                    if input[3] < 37.38889_f64 {
                        var79 = 0.010663435_f64;
                    } else {
                        var79 = -0.011382141_f64;
                    }
                } else {
                    if input[10] < 0.34461153_f64 {
                        var79 = -0.054163434_f64;
                    } else {
                        var79 = -0.0122908745_f64;
                    }
                }
            } else {
                if input[12] < 0.24758221_f64 {
                    if input[22] < 3.5597324_f64 {
                        var79 = -0.011609283_f64;
                    } else {
                        var79 = 0.00012281144_f64;
                    }
                } else {
                    if input[11] < 0.07709251_f64 {
                        var79 = -0.030750856_f64;
                    } else {
                        var79 = -0.006670763_f64;
                    }
                }
            }
        }
    } else {
        if input[1] < 2.447644_f64 {
            if input[22] < 7.5069256_f64 {
                if input[35] < 18.02482_f64 {
                    if input[35] < 17.499226_f64 {
                        var79 = -0.007329651_f64;
                    } else {
                        var79 = 0.012692002_f64;
                    }
                } else {
                    if input[22] < 6.941912_f64 {
                        var79 = 0.0043130796_f64;
                    } else {
                        var79 = -0.0085624_f64;
                    }
                }
            } else {
                if input[11] < 0.19193427_f64 {
                    if input[10] < 0.16658017_f64 {
                        var79 = -0.002240575_f64;
                    } else {
                        var79 = 0.01007801_f64;
                    }
                } else {
                    if input[3] < 1738.6666_f64 {
                        var79 = 0.01923452_f64;
                    } else {
                        var79 = 0.0027193509_f64;
                    }
                }
            }
        } else {
            if input[26] < 2.9937801_f64 {
                if input[35] < 18.515_f64 {
                    if input[22] < 7.0782166_f64 {
                        var79 = -0.009047156_f64;
                    } else {
                        var79 = 0.009139247_f64;
                    }
                } else {
                    if input[2] < 16.0_f64 {
                        var79 = -0.0107429605_f64;
                    } else {
                        var79 = -0.04844807_f64;
                    }
                }
            } else {
                if input[10] < 0.2961165_f64 {
                    if input[1] < 10.697594_f64 {
                        var79 = 0.0027401557_f64;
                    } else {
                        var79 = -0.0010903082_f64;
                    }
                } else {
                    if input[3] < 758.7619_f64 {
                        var79 = -0.008033298_f64;
                    } else {
                        var79 = 0.0016736707_f64;
                    }
                }
            }
        }
    }
    let var80: f64;
    if input[12] < 0.09598741_f64 {
        if input[15] < 39.0_f64 {
            if input[8] < 2298.0_f64 {
                if input[1] < 4.0369134_f64 {
                    if input[11] < 0.22365038_f64 {
                        var80 = -0.005911562_f64;
                    } else {
                        var80 = 0.007307583_f64;
                    }
                } else {
                    if input[10] < 0.1463964_f64 {
                        var80 = -0.022988463_f64;
                    } else {
                        var80 = -0.0018540215_f64;
                    }
                }
            } else {
                if input[7] < 642.0_f64 {
                    if input[2] < 75.0_f64 {
                        var80 = -0.035099518_f64;
                    } else {
                        var80 = 0.0015651205_f64;
                    }
                } else {
                    if input[20] < 20.405575_f64 {
                        var80 = -0.017641483_f64;
                    } else {
                        var80 = 0.00026944905_f64;
                    }
                }
            }
        } else {
            if input[33] < 60127.0_f64 {
                if input[0] < 2313.0_f64 {
                    if input[4] < 7148.0_f64 {
                        var80 = 0.0017454186_f64;
                    } else {
                        var80 = -0.01632356_f64;
                    }
                } else {
                    if input[7] < 95.0_f64 {
                        var80 = 0.0052047_f64;
                    } else {
                        var80 = 0.024675865_f64;
                    }
                }
            } else {
                if input[5] < 1227.0_f64 {
                    if input[30] < 19.0_f64 {
                        var80 = -0.0017426389_f64;
                    } else {
                        var80 = -0.028970188_f64;
                    }
                } else {
                    if input[13] < 0.45012164_f64 {
                        var80 = 0.007917398_f64;
                    } else {
                        var80 = -0.021518316_f64;
                    }
                }
            }
        }
    } else {
        if input[15] < 30.0_f64 {
            if input[20] < 17.745762_f64 {
                if input[10] < 0.14970563_f64 {
                    if input[19] < 153.02295_f64 {
                        var80 = 0.00016785176_f64;
                    } else {
                        var80 = -0.003996008_f64;
                    }
                } else {
                    if input[12] < 0.2265861_f64 {
                        var80 = 0.0010293815_f64;
                    } else {
                        var80 = 0.0022251157_f64;
                    }
                }
            } else {
                if input[13] < 0.3508772_f64 {
                    if input[1] < 3.7526042_f64 {
                        var80 = -0.027423495_f64;
                    } else {
                        var80 = 0.0067017362_f64;
                    }
                } else {
                    if input[1] < 1.6584686_f64 {
                        var80 = 0.018698718_f64;
                    } else {
                        var80 = -0.0070800274_f64;
                    }
                }
            }
        } else {
            if input[16] < 25.600283_f64 {
                if input[15] < 32.0_f64 {
                    if input[11] < 0.115555555_f64 {
                        var80 = 0.020825451_f64;
                    } else {
                        var80 = 0.006989617_f64;
                    }
                } else {
                    if input[6] < 87.0_f64 {
                        var80 = -0.011379235_f64;
                    } else {
                        var80 = 0.0018008149_f64;
                    }
                }
            } else {
                if input[12] < 0.28242075_f64 {
                    if input[10] < 0.07663783_f64 {
                        var80 = -0.0065560914_f64;
                    } else {
                        var80 = 0.0017527873_f64;
                    }
                } else {
                    if input[22] < 4.8675985_f64 {
                        var80 = 0.012999931_f64;
                    } else {
                        var80 = 0.0030727373_f64;
                    }
                }
            }
        }
    }
    let var81: f64;
    if input[30] < 10.0_f64 {
        if input[11] < 0.102564104_f64 {
            if input[4] < 10674.0_f64 {
                if input[2] < 56.0_f64 {
                    if input[4] < 5595.0_f64 {
                        var81 = -0.0040712017_f64;
                    } else {
                        var81 = -0.029801074_f64;
                    }
                } else {
                    if input[12] < 0.14594595_f64 {
                        var81 = -0.019050859_f64;
                    } else {
                        var81 = 0.004653345_f64;
                    }
                }
            } else {
                if input[12] < 0.19178082_f64 {
                    var81 = 0.0073516006_f64;
                } else {
                    if input[3] < 6042.5454_f64 {
                        var81 = -0.013838964_f64;
                    } else {
                        var81 = -0.041954983_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.3019608_f64 {
                if input[13] < 0.41893157_f64 {
                    if input[4] < 1812.0_f64 {
                        var81 = -0.0020782833_f64;
                    } else {
                        var81 = 0.0012387567_f64;
                    }
                } else {
                    if input[1] < 2.5158632_f64 {
                        var81 = 0.012349673_f64;
                    } else {
                        var81 = -0.0026685996_f64;
                    }
                }
            } else {
                if input[2] < 89.0_f64 {
                    if input[3] < 4740.636_f64 {
                        var81 = -0.004038567_f64;
                    } else {
                        var81 = -0.028297096_f64;
                    }
                } else {
                    if input[5] < 147.0_f64 {
                        var81 = 0.020943573_f64;
                    } else {
                        var81 = -0.005594428_f64;
                    }
                }
            }
        }
    } else {
        if input[10] < 0.27865613_f64 {
            if input[11] < 0.18328841_f64 {
                if input[25] < 0.00030379987_f64 {
                    if input[10] < 0.27670753_f64 {
                        var81 = 0.010968504_f64;
                    } else {
                        var81 = -0.016396763_f64;
                    }
                } else {
                    if input[5] < 49.0_f64 {
                        var81 = -0.0073444988_f64;
                    } else {
                        var81 = 0.0023254005_f64;
                    }
                }
            } else {
                if input[29] < 352.0_f64 {
                    if input[13] < 0.47155812_f64 {
                        var81 = 0.0009197641_f64;
                    } else {
                        var81 = -0.015587873_f64;
                    }
                } else {
                    if input[5] < 400.0_f64 {
                        var81 = 0.0053504487_f64;
                    } else {
                        var81 = 0.0014915811_f64;
                    }
                }
            }
        } else {
            if input[35] < 17.74646_f64 {
                if input[2] < 87.0_f64 {
                    if input[1] < 5.8154483_f64 {
                        var81 = -0.00039542792_f64;
                    } else {
                        var81 = -0.004700456_f64;
                    }
                } else {
                    if input[6] < 242.0_f64 {
                        var81 = -0.00066145096_f64;
                    } else {
                        var81 = 0.008168901_f64;
                    }
                }
            } else {
                if input[22] < 3.8806787_f64 {
                    if input[35] < 18.548388_f64 {
                        var81 = 0.0005163346_f64;
                    } else {
                        var81 = -0.015628971_f64;
                    }
                } else {
                    if input[11] < 0.2656396_f64 {
                        var81 = 0.0012763494_f64;
                    } else {
                        var81 = -0.003881108_f64;
                    }
                }
            }
        }
    }
    let var82: f64;
    if input[10] < 0.35_f64 {
        if input[30] < 14.0_f64 {
            if input[2] < 10.0_f64 {
                if input[10] < 0.32578397_f64 {
                    if input[22] < 6.4267254_f64 {
                        var82 = 0.0029885916_f64;
                    } else {
                        var82 = 0.011284864_f64;
                    }
                } else {
                    if input[11] < 0.15181269_f64 {
                        var82 = 0.0028660335_f64;
                    } else {
                        var82 = -0.027571535_f64;
                    }
                }
            } else {
                if input[11] < 0.3178114_f64 {
                    if input[10] < 0.24009325_f64 {
                        var82 = 0.0011226434_f64;
                    } else {
                        var82 = 0.00004549163_f64;
                    }
                } else {
                    if input[13] < 0.36910197_f64 {
                        var82 = 0.00027063204_f64;
                    } else {
                        var82 = -0.007142848_f64;
                    }
                }
            }
        } else {
            if input[13] < 0.42390525_f64 {
                if input[11] < 0.21907601_f64 {
                    if input[6] < 246.0_f64 {
                        var82 = 0.0015533554_f64;
                    } else {
                        var82 = 0.0026836907_f64;
                    }
                } else {
                    if input[16] < 21.78718_f64 {
                        var82 = -0.004978134_f64;
                    } else {
                        var82 = 0.001242733_f64;
                    }
                }
            } else {
                if input[6] < 616.0_f64 {
                    if input[11] < 0.20884658_f64 {
                        var82 = 0.00025811745_f64;
                    } else {
                        var82 = -0.003288071_f64;
                    }
                } else {
                    if input[20] < 19.35792_f64 {
                        var82 = 0.007664261_f64;
                    } else {
                        var82 = 0.0009830131_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.19414414_f64 {
            if input[24] < 86186.0_f64 {
                if input[19] < 238.91722_f64 {
                    if input[0] < 2850.0_f64 {
                        var82 = 0.0007634077_f64;
                    } else {
                        var82 = 0.017246444_f64;
                    }
                } else {
                    if input[19] < 243.38016_f64 {
                        var82 = -0.0435513_f64;
                    } else {
                        var82 = -0.0037721817_f64;
                    }
                }
            } else {
                if input[12] < 0.15820895_f64 {
                    if input[12] < 0.1473772_f64 {
                        var82 = -0.0045996397_f64;
                    } else {
                        var82 = -0.022396684_f64;
                    }
                } else {
                    if input[2] < 91.0_f64 {
                        var82 = 0.008030082_f64;
                    } else {
                        var82 = -0.0039677164_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.19774719_f64 {
                if input[22] < 6.4842277_f64 {
                    if input[2] < 61.0_f64 {
                        var82 = -0.04959214_f64;
                    } else {
                        var82 = -0.011454033_f64;
                    }
                } else {
                    if input[2] < 18.0_f64 {
                        var82 = 0.004847751_f64;
                    } else {
                        var82 = -0.0073061134_f64;
                    }
                }
            } else {
                if input[26] < 84.26858_f64 {
                    if input[11] < 0.06720161_f64 {
                        var82 = 0.010021161_f64;
                    } else {
                        var82 = -0.009059015_f64;
                    }
                } else {
                    if input[1] < 4.145958_f64 {
                        var82 = -0.0045023663_f64;
                    } else {
                        var82 = 0.015161_f64;
                    }
                }
            }
        }
    }
    let var83: f64;
    if input[30] < 18.0_f64 {
        if input[35] < 17.271885_f64 {
            if input[13] < 0.4398977_f64 {
                if input[12] < 0.08949079_f64 {
                    if input[2] < 62.0_f64 {
                        var83 = 0.0044869254_f64;
                    } else {
                        var83 = 0.01657132_f64;
                    }
                } else {
                    if input[12] < 0.10612245_f64 {
                        var83 = -0.025883308_f64;
                    } else {
                        var83 = -0.0052465126_f64;
                    }
                }
            } else {
                if input[7] < 29.0_f64 {
                    var83 = -0.029016813_f64;
                } else {
                    if input[4] < 337.0_f64 {
                        var83 = 0.014990156_f64;
                    } else {
                        var83 = -0.00030416934_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.33045977_f64 {
                if input[12] < 0.08512975_f64 {
                    if input[6] < 1214.0_f64 {
                        var83 = -0.0010712185_f64;
                    } else {
                        var83 = -0.013965564_f64;
                    }
                } else {
                    if input[13] < 0.30356118_f64 {
                        var83 = -0.0008584582_f64;
                    } else {
                        var83 = 0.0011225881_f64;
                    }
                }
            } else {
                if input[35] < 18.11701_f64 {
                    if input[3] < 1100.9048_f64 {
                        var83 = 0.005947552_f64;
                    } else {
                        var83 = -0.036834735_f64;
                    }
                } else {
                    if input[13] < 0.4144621_f64 {
                        var83 = -0.0014903651_f64;
                    } else {
                        var83 = 0.015092611_f64;
                    }
                }
            }
        }
    } else {
        if input[16] < 44.547756_f64 {
            if input[19] < 583.9337_f64 {
                if input[1] < 6.83554_f64 {
                    if input[1] < 6.4869747_f64 {
                        var83 = 0.0018968629_f64;
                    } else {
                        var83 = 0.004967726_f64;
                    }
                } else {
                    if input[4] < 3781.0_f64 {
                        var83 = 0.0038376593_f64;
                    } else {
                        var83 = 0.0005731561_f64;
                    }
                }
            } else {
                if input[4] < 10462.0_f64 {
                    if input[22] < 7.2779803_f64 {
                        var83 = -0.006312325_f64;
                    } else {
                        var83 = -0.04548864_f64;
                    }
                } else {
                    if input[1] < 5.43827_f64 {
                        var83 = 0.011821184_f64;
                    } else {
                        var83 = 0.00056280836_f64;
                    }
                }
            }
        } else {
            if input[7] < 1327.0_f64 {
                if input[12] < 0.19014627_f64 {
                    if input[24] < 87334.0_f64 {
                        var83 = -0.030996934_f64;
                    } else {
                        var83 = 0.00081391603_f64;
                    }
                } else {
                    if input[13] < 0.32627118_f64 {
                        var83 = 0.016710622_f64;
                    } else {
                        var83 = 0.0039854157_f64;
                    }
                }
            } else {
                if input[11] < 0.27228683_f64 {
                    if input[4] < 4355.0_f64 {
                        var83 = 0.015492702_f64;
                    } else {
                        var83 = 0.0034440176_f64;
                    }
                } else {
                    if input[3] < 4819.3184_f64 {
                        var83 = 0.023236249_f64;
                    } else {
                        var83 = 0.006172992_f64;
                    }
                }
            }
        }
    }
    let var84: f64;
    if input[30] < 10.0_f64 {
        if input[33] < 169076.0_f64 {
            if input[19] < 340.42465_f64 {
                if input[3] < 6042.5454_f64 {
                    if input[3] < 5616.591_f64 {
                        var84 = -0.00025716223_f64;
                    } else {
                        var84 = 0.0071497755_f64;
                    }
                } else {
                    if input[20] < 10.14724_f64 {
                        var84 = 0.012311316_f64;
                    } else {
                        var84 = -0.008443017_f64;
                    }
                }
            } else {
                if input[15] < 34.0_f64 {
                    var84 = -0.010058165_f64;
                } else {
                    var84 = -0.05306496_f64;
                }
            }
        } else {
            if input[4] < 10530.0_f64 {
                if input[19] < 304.4012_f64 {
                    var84 = -0.022376671_f64;
                } else {
                    if input[0] < 18475.0_f64 {
                        var84 = 0.021217445_f64;
                    } else {
                        var84 = -0.01648376_f64;
                    }
                }
            } else {
                if input[1] < 7.353603_f64 {
                    if input[25] < 0.00068372575_f64 {
                        var84 = -0.028273553_f64;
                    } else {
                        var84 = -0.00964284_f64;
                    }
                } else {
                    if input[0] < 11593.0_f64 {
                        var84 = 0.0069013583_f64;
                    } else {
                        var84 = 0.0012214076_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.26113904_f64 {
            if input[10] < 0.15306123_f64 {
                if input[1] < 10.813974_f64 {
                    if input[22] < 7.3555303_f64 {
                        var84 = -0.0008204532_f64;
                    } else {
                        var84 = 0.0038928303_f64;
                    }
                } else {
                    if input[2] < 99.0_f64 {
                        var84 = 0.008877528_f64;
                    } else {
                        var84 = -0.018104684_f64;
                    }
                }
            } else {
                if input[13] < 0.30356118_f64 {
                    if input[5] < 363.0_f64 {
                        var84 = -0.0033076953_f64;
                    } else {
                        var84 = 0.0012987107_f64;
                    }
                } else {
                    if input[13] < 0.405954_f64 {
                        var84 = 0.0013118178_f64;
                    } else {
                        var84 = 0.00039597586_f64;
                    }
                }
            }
        } else {
            if input[26] < 7.902406_f64 {
                if input[10] < 0.110275686_f64 {
                    if input[11] < 0.21616541_f64 {
                        var84 = -0.011764713_f64;
                    } else {
                        var84 = 0.0017851604_f64;
                    }
                } else {
                    if input[35] < 19.599268_f64 {
                        var84 = 0.006351934_f64;
                    } else {
                        var84 = -0.0024920206_f64;
                    }
                }
            } else {
                if input[11] < 0.08375_f64 {
                    if input[4] < 11689.0_f64 {
                        var84 = -0.004873733_f64;
                    } else {
                        var84 = 0.012126103_f64;
                    }
                } else {
                    if input[19] < 458.39038_f64 {
                        var84 = 0.0017548818_f64;
                    } else {
                        var84 = -0.012570338_f64;
                    }
                }
            }
        }
    }
    let var85: f64;
    if input[10] < 0.35_f64 {
        if input[5] < 108.0_f64 {
            if input[20] < 13.557312_f64 {
                if input[30] < 17.0_f64 {
                    if input[4] < 11144.0_f64 {
                        var85 = 0.000088772766_f64;
                    } else {
                        var85 = 0.0033714378_f64;
                    }
                } else {
                    if input[2] < 84.0_f64 {
                        var85 = 0.00308354_f64;
                    } else {
                        var85 = 0.013653788_f64;
                    }
                }
            } else {
                if input[22] < 4.5699797_f64 {
                    if input[6] < 127.0_f64 {
                        var85 = -0.024457997_f64;
                    } else {
                        var85 = -0.002893024_f64;
                    }
                } else {
                    if input[4] < 8706.0_f64 {
                        var85 = -0.0001256315_f64;
                    } else {
                        var85 = -0.004156634_f64;
                    }
                }
            }
        } else {
            if input[23] < 350.0_f64 {
                var85 = -0.043516744_f64;
            } else {
                if input[13] < 0.39241052_f64 {
                    if input[13] < 0.35739437_f64 {
                        var85 = 0.00077673513_f64;
                    } else {
                        var85 = 0.0017690432_f64;
                    }
                } else {
                    if input[7] < 1212.0_f64 {
                        var85 = 0.00033615335_f64;
                    } else {
                        var85 = 0.003339144_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.18775101_f64 {
            if input[4] < 7772.0_f64 {
                if input[22] < 3.7963536_f64 {
                    if input[12] < 0.13118812_f64 {
                        var85 = -0.0011861629_f64;
                    } else {
                        var85 = -0.023960996_f64;
                    }
                } else {
                    if input[6] < 658.0_f64 {
                        var85 = 0.0017115775_f64;
                    } else {
                        var85 = -0.0056416737_f64;
                    }
                }
            } else {
                if input[35] < 17.109346_f64 {
                    var85 = -0.04426519_f64;
                } else {
                    if input[13] < 0.2934363_f64 {
                        var85 = -0.019282054_f64;
                    } else {
                        var85 = -0.0023503865_f64;
                    }
                }
            }
        } else {
            if input[24] < 78196.0_f64 {
                if input[22] < 6.6296387_f64 {
                    if input[22] < 6.329843_f64 {
                        var85 = -0.0112687_f64;
                    } else {
                        var85 = -0.035859387_f64;
                    }
                } else {
                    if input[22] < 6.876038_f64 {
                        var85 = 0.012054753_f64;
                    } else {
                        var85 = -0.014087482_f64;
                    }
                }
            } else {
                if input[10] < 0.35634327_f64 {
                    if input[2] < 84.0_f64 {
                        var85 = 0.017128054_f64;
                    } else {
                        var85 = 0.000111265224_f64;
                    }
                } else {
                    if input[11] < 0.09953704_f64 {
                        var85 = 0.004993886_f64;
                    } else {
                        var85 = -0.015338115_f64;
                    }
                }
            }
        }
    }
    let var86: f64;
    if input[10] < 0.27865613_f64 {
        if input[11] < 0.18089172_f64 {
            if input[11] < 0.12060302_f64 {
                if input[26] < 7.3177457_f64 {
                    if input[22] < 5.9708714_f64 {
                        var86 = 0.0002262293_f64;
                    } else {
                        var86 = 0.00942463_f64;
                    }
                } else {
                    if input[19] < 43.5507_f64 {
                        var86 = -0.030117933_f64;
                    } else {
                        var86 = -0.0005178902_f64;
                    }
                }
            } else {
                if input[7] < 651.0_f64 {
                    if input[0] < 2429.0_f64 {
                        var86 = 0.0018364455_f64;
                    } else {
                        var86 = -0.0021377741_f64;
                    }
                } else {
                    if input[20] < 18.558805_f64 {
                        var86 = 0.0058406214_f64;
                    } else {
                        var86 = 0.002139305_f64;
                    }
                }
            }
        } else {
            if input[22] < 4.354329_f64 {
                if input[19] < 80.8366_f64 {
                    if input[6] < 162.0_f64 {
                        var86 = 0.00037419246_f64;
                    } else {
                        var86 = 0.009195867_f64;
                    }
                } else {
                    if input[19] < 81.44889_f64 {
                        var86 = -0.017563373_f64;
                    } else {
                        var86 = -0.0019005539_f64;
                    }
                }
            } else {
                if input[35] < 16.951084_f64 {
                    if input[4] < 3921.0_f64 {
                        var86 = -0.033575_f64;
                    } else {
                        var86 = -0.0051891017_f64;
                    }
                } else {
                    if input[19] < 67.94796_f64 {
                        var86 = -0.0019479608_f64;
                    } else {
                        var86 = 0.0008221646_f64;
                    }
                }
            }
        }
    } else {
        if input[15] < 33.0_f64 {
            if input[19] < 281.8234_f64 {
                if input[11] < 0.19854721_f64 {
                    if input[2] < 86.0_f64 {
                        var86 = -0.0014877504_f64;
                    } else {
                        var86 = 0.0017719277_f64;
                    }
                } else {
                    if input[22] < 3.8389022_f64 {
                        var86 = -0.010225628_f64;
                    } else {
                        var86 = 0.0020739574_f64;
                    }
                }
            } else {
                if input[26] < 19.367033_f64 {
                    if input[1] < 9.026796_f64 {
                        var86 = -0.0189621_f64;
                    } else {
                        var86 = 0.0071194232_f64;
                    }
                } else {
                    if input[7] < 839.0_f64 {
                        var86 = -0.016642509_f64;
                    } else {
                        var86 = -0.053506084_f64;
                    }
                }
            }
        } else {
            if input[6] < 854.0_f64 {
                if input[35] < 19.862576_f64 {
                    if input[22] < 7.0782166_f64 {
                        var86 = 0.0032452985_f64;
                    } else {
                        var86 = -0.00008335184_f64;
                    }
                } else {
                    if input[8] < 300.0_f64 {
                        var86 = -0.047619212_f64;
                    } else {
                        var86 = -0.0069456147_f64;
                    }
                }
            } else {
                if input[16] < 38.44282_f64 {
                    if input[19] < 360.36847_f64 {
                        var86 = -0.003041659_f64;
                    } else {
                        var86 = -0.0136694135_f64;
                    }
                } else {
                    if input[20] < 22.337288_f64 {
                        var86 = 0.008461244_f64;
                    } else {
                        var86 = -0.000472_f64;
                    }
                }
            }
        }
    }
    let var87: f64;
    if input[3] < 81.210526_f64 {
        if input[17] < 3350.0_f64 {
            if input[22] < 7.0782166_f64 {
                if input[10] < 0.3643846_f64 {
                    if input[12] < 0.10382322_f64 {
                        var87 = 0.013252163_f64;
                    } else {
                        var87 = 0.002536184_f64;
                    }
                } else {
                    var87 = -0.019133732_f64;
                }
            } else {
                if input[5] < 366.0_f64 {
                    if input[25] < 0.0020526187_f64 {
                        var87 = 0.017486095_f64;
                    } else {
                        var87 = 0.005261274_f64;
                    }
                } else {
                    if input[4] < 136.0_f64 {
                        var87 = -0.0034732146_f64;
                    } else {
                        var87 = 0.0038272613_f64;
                    }
                }
            }
        } else {
            if input[5] < 524.0_f64 {
                if input[29] < 345.0_f64 {
                    var87 = 0.0064789774_f64;
                } else {
                    var87 = 0.02318643_f64;
                }
            } else {
                var87 = 0.0051810914_f64;
            }
        }
    } else {
        if input[24] < 3996.0_f64 {
            if input[4] < 236.0_f64 {
                if input[12] < 0.20179372_f64 {
                    if input[24] < 2467.0_f64 {
                        var87 = -0.03744344_f64;
                    } else {
                        var87 = -0.0052958177_f64;
                    }
                } else {
                    if input[17] < 3621.0_f64 {
                        var87 = 0.0017366965_f64;
                    } else {
                        var87 = 0.021400027_f64;
                    }
                }
            } else {
                if input[5] < 210.0_f64 {
                    if input[3] < 101.65_f64 {
                        var87 = 0.0063934885_f64;
                    } else {
                        var87 = -0.030142387_f64;
                    }
                } else {
                    if input[22] < 6.8544707_f64 {
                        var87 = -0.027491141_f64;
                    } else {
                        var87 = 0.0034857013_f64;
                    }
                }
            }
        } else {
            if input[15] < 26.0_f64 {
                if input[10] < 0.15673469_f64 {
                    if input[25] < 0.004326864_f64 {
                        var87 = -0.030384151_f64;
                    } else {
                        var87 = -0.0015482333_f64;
                    }
                } else {
                    if input[20] < 16.96525_f64 {
                        var87 = 0.00038033046_f64;
                    } else {
                        var87 = -0.035158228_f64;
                    }
                }
            } else {
                if input[20] < 14.527063_f64 {
                    if input[19] < 110.707466_f64 {
                        var87 = 0.0014619207_f64;
                    } else {
                        var87 = 0.004979136_f64;
                    }
                } else {
                    if input[22] < 4.189326_f64 {
                        var87 = -0.00829844_f64;
                    } else {
                        var87 = 0.00072604365_f64;
                    }
                }
            }
        }
    }
    let var88: f64;
    if input[12] < 0.09598741_f64 {
        if input[15] < 39.0_f64 {
            if input[8] < 2298.0_f64 {
                if input[1] < 4.0369134_f64 {
                    if input[11] < 0.22365038_f64 {
                        var88 = -0.0055466457_f64;
                    } else {
                        var88 = 0.0061823535_f64;
                    }
                } else {
                    if input[10] < 0.1463964_f64 {
                        var88 = -0.020185744_f64;
                    } else {
                        var88 = -0.0019913213_f64;
                    }
                }
            } else {
                if input[7] < 642.0_f64 {
                    if input[2] < 75.0_f64 {
                        var88 = -0.03010956_f64;
                    } else {
                        var88 = 0.0013996955_f64;
                    }
                } else {
                    if input[30] < 15.0_f64 {
                        var88 = 0.001305411_f64;
                    } else {
                        var88 = -0.015581968_f64;
                    }
                }
            }
        } else {
            if input[13] < 0.40233237_f64 {
                if input[13] < 0.39444613_f64 {
                    if input[4] < 2146.0_f64 {
                        var88 = -0.007909616_f64;
                    } else {
                        var88 = 0.0050126044_f64;
                    }
                } else {
                    if input[4] < 4355.0_f64 {
                        var88 = -0.0015802985_f64;
                    } else {
                        var88 = -0.025008684_f64;
                    }
                }
            } else {
                if input[1] < 7.7323194_f64 {
                    if input[5] < 2562.0_f64 {
                        var88 = 0.018281195_f64;
                    } else {
                        var88 = 0.0021809526_f64;
                    }
                } else {
                    if input[10] < 0.2831126_f64 {
                        var88 = -0.019480964_f64;
                    } else {
                        var88 = 0.013939465_f64;
                    }
                }
            }
        }
    } else {
        if input[11] < 0.33045977_f64 {
            if input[3] < 37.38889_f64 {
                if input[6] < 119.0_f64 {
                    if input[25] < 0.006695871_f64 {
                        var88 = -0.00037571948_f64;
                    } else {
                        var88 = 0.012313767_f64;
                    }
                } else {
                    if input[12] < 0.12776025_f64 {
                        var88 = -0.013102569_f64;
                    } else {
                        var88 = 0.0105381925_f64;
                    }
                }
            } else {
                if input[15] < 36.0_f64 {
                    if input[13] < 0.39241052_f64 {
                        var88 = 0.00082753814_f64;
                    } else {
                        var88 = 0.000062924475_f64;
                    }
                } else {
                    if input[19] < 135.2604_f64 {
                        var88 = -0.0072266483_f64;
                    } else {
                        var88 = 0.0015626792_f64;
                    }
                }
            }
        } else {
            if input[8] < 261.0_f64 {
                if input[8] < 240.0_f64 {
                    if input[16] < 28.469803_f64 {
                        var88 = -0.0018123736_f64;
                    } else {
                        var88 = -0.018656397_f64;
                    }
                } else {
                    if input[16] < 27.034433_f64 {
                        var88 = -0.04152674_f64;
                    } else {
                        var88 = -0.001310421_f64;
                    }
                }
            } else {
                if input[10] < 0.10353011_f64 {
                    if input[26] < 31.340298_f64 {
                        var88 = -0.014362319_f64;
                    } else {
                        var88 = 0.0050494573_f64;
                    }
                } else {
                    if input[4] < 2614.0_f64 {
                        var88 = 0.005561313_f64;
                    } else {
                        var88 = -0.00074727257_f64;
                    }
                }
            }
        }
    }
    let var89: f64;
    if input[10] < 0.27865613_f64 {
        if input[11] < 0.20651747_f64 {
            if input[1] < 9.543416_f64 {
                if input[0] < 5632.0_f64 {
                    if input[16] < 17.243782_f64 {
                        var89 = -0.006925858_f64;
                    } else {
                        var89 = 0.0011937944_f64;
                    }
                } else {
                    if input[4] < 11797.0_f64 {
                        var89 = 0.004159361_f64;
                    } else {
                        var89 = -0.0068384386_f64;
                    }
                }
            } else {
                if input[10] < 0.12306531_f64 {
                    if input[15] < 25.0_f64 {
                        var89 = -0.042949762_f64;
                    } else {
                        var89 = -0.006439028_f64;
                    }
                } else {
                    if input[10] < 0.22151224_f64 {
                        var89 = 0.0017117037_f64;
                    } else {
                        var89 = -0.0022262153_f64;
                    }
                }
            }
        } else {
            if input[13] < 0.4074074_f64 {
                if input[10] < 0.1252372_f64 {
                    if input[7] < 66.0_f64 {
                        var89 = -0.03164582_f64;
                    } else {
                        var89 = -0.0010782364_f64;
                    }
                } else {
                    if input[15] < 28.0_f64 {
                        var89 = 0.00004852477_f64;
                    } else {
                        var89 = 0.0010392354_f64;
                    }
                }
            } else {
                if input[15] < 36.0_f64 {
                    if input[16] < 31.267494_f64 {
                        var89 = -0.001113137_f64;
                    } else {
                        var89 = -0.0047828197_f64;
                    }
                } else {
                    if input[13] < 0.41504306_f64 {
                        var89 = -0.0039251214_f64;
                    } else {
                        var89 = 0.0034303423_f64;
                    }
                }
            }
        }
    } else {
        if input[13] < 0.42833108_f64 {
            if input[15] < 33.0_f64 {
                if input[19] < 281.8234_f64 {
                    if input[11] < 0.19377568_f64 {
                        var89 = -0.0009371224_f64;
                    } else {
                        var89 = 0.0011857124_f64;
                    }
                } else {
                    if input[26] < 19.367033_f64 {
                        var89 = -0.013278969_f64;
                    } else {
                        var89 = -0.040557567_f64;
                    }
                }
            } else {
                if input[6] < 920.0_f64 {
                    if input[35] < 19.862576_f64 {
                        var89 = 0.0021650523_f64;
                    } else {
                        var89 = -0.013684066_f64;
                    }
                } else {
                    if input[8] < 2059.0_f64 {
                        var89 = -0.007408549_f64;
                    } else {
                        var89 = 0.0004793956_f64;
                    }
                }
            }
        } else {
            if input[35] < 17.3022_f64 {
                if input[1] < 9.431322_f64 {
                    if input[22] < 6.1650395_f64 {
                        var89 = -0.0014952347_f64;
                    } else {
                        var89 = -0.009466175_f64;
                    }
                } else {
                    if input[15] < 27.0_f64 {
                        var89 = -0.02043461_f64;
                    } else {
                        var89 = 0.012729542_f64;
                    }
                }
            } else {
                if input[22] < 5.005065_f64 {
                    var89 = -0.0066637597_f64;
                } else {
                    var89 = -0.036736_f64;
                }
            }
        }
    }
    let var90: f64;
    if input[11] < 0.08375_f64 {
        if input[2] < 41.0_f64 {
            if input[4] < 4396.0_f64 {
                if input[12] < 0.33746272_f64 {
                    if input[6] < 58.0_f64 {
                        var90 = -0.008062049_f64;
                    } else {
                        var90 = 0.0017245669_f64;
                    }
                } else {
                    if input[4] < 898.0_f64 {
                        var90 = 0.0020314066_f64;
                    } else {
                        var90 = -0.02586156_f64;
                    }
                }
            } else {
                if input[16] < 36.40073_f64 {
                    if input[4] < 4815.0_f64 {
                        var90 = -0.028841479_f64;
                    } else {
                        var90 = -0.004747361_f64;
                    }
                } else {
                    if input[13] < 0.36070383_f64 {
                        var90 = -0.08172616_f64;
                    } else {
                        var90 = -0.015780343_f64;
                    }
                }
            }
        } else {
            if input[7] < 519.0_f64 {
                if input[35] < 18.1043_f64 {
                    if input[1] < 8.135564_f64 {
                        var90 = 0.002705174_f64;
                    } else {
                        var90 = -0.007330764_f64;
                    }
                } else {
                    if input[13] < 0.2960822_f64 {
                        var90 = 0.0072316374_f64;
                    } else {
                        var90 = -0.013132135_f64;
                    }
                }
            } else {
                if input[35] < 16.79554_f64 {
                    if input[3] < 5052.3184_f64 {
                        var90 = 0.021940766_f64;
                    } else {
                        var90 = 0.008177522_f64;
                    }
                } else {
                    if input[13] < 0.37594503_f64 {
                        var90 = 0.008812311_f64;
                    } else {
                        var90 = -0.0023252992_f64;
                    }
                }
            }
        }
    } else {
        if input[12] < 0.24329026_f64 {
            if input[30] < 16.0_f64 {
                if input[11] < 0.124938026_f64 {
                    if input[8] < 316.0_f64 {
                        var90 = 0.0012769302_f64;
                    } else {
                        var90 = -0.0033024487_f64;
                    }
                } else {
                    if input[19] < 43.5507_f64 {
                        var90 = -0.005460931_f64;
                    } else {
                        var90 = 0.00024965868_f64;
                    }
                }
            } else {
                if input[10] < 0.17336395_f64 {
                    if input[13] < 0.2986111_f64 {
                        var90 = 0.010868986_f64;
                    } else {
                        var90 = -0.00081229955_f64;
                    }
                } else {
                    if input[10] < 0.37548056_f64 {
                        var90 = 0.0011671998_f64;
                    } else {
                        var90 = -0.005654545_f64;
                    }
                }
            }
        } else {
            if input[13] < 0.3153786_f64 {
                if input[35] < 19.100538_f64 {
                    if input[4] < 5070.0_f64 {
                        var90 = -0.0212359_f64;
                    } else {
                        var90 = -0.0052419286_f64;
                    }
                } else {
                    if input[10] < 0.110275686_f64 {
                        var90 = -0.011091018_f64;
                    } else {
                        var90 = -0.00011957857_f64;
                    }
                }
            } else {
                if input[19] < 181.36148_f64 {
                    if input[20] < 16.699358_f64 {
                        var90 = 0.0013394154_f64;
                    } else {
                        var90 = -0.0012355432_f64;
                    }
                } else {
                    if input[10] < 0.07663783_f64 {
                        var90 = -0.0067972117_f64;
                    } else {
                        var90 = 0.002717553_f64;
                    }
                }
            }
        }
    }
    let var91: f64;
    if input[15] < 45.0_f64 {
        if input[12] < 0.08512975_f64 {
            if input[10] < 0.1463964_f64 {
                if input[1] < 5.838965_f64 {
                    if input[1] < 4.5170293_f64 {
                        var91 = -0.015530047_f64;
                    } else {
                        var91 = 0.022731777_f64;
                    }
                } else {
                    if input[0] < 1173.0_f64 {
                        var91 = -0.014074047_f64;
                    } else {
                        var91 = -0.049695827_f64;
                    }
                }
            } else {
                if input[11] < 0.34256172_f64 {
                    if input[6] < 1214.0_f64 {
                        var91 = -0.0013815885_f64;
                    } else {
                        var91 = -0.009133159_f64;
                    }
                } else {
                    if input[15] < 24.0_f64 {
                        var91 = -0.016078183_f64;
                    } else {
                        var91 = 0.0077662724_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.34256172_f64 {
                if input[4] < 86.0_f64 {
                    if input[6] < 161.0_f64 {
                        var91 = 0.0025347015_f64;
                    } else {
                        var91 = 0.0112658_f64;
                    }
                } else {
                    if input[11] < 0.12060302_f64 {
                        var91 = -0.0005541518_f64;
                    } else {
                        var91 = 0.0005547559_f64;
                    }
                }
            } else {
                if input[1] < 7.9223404_f64 {
                    if input[3] < 3591.8096_f64 {
                        var91 = -0.0024870585_f64;
                    } else {
                        var91 = 0.0040528416_f64;
                    }
                } else {
                    if input[26] < 57.339706_f64 {
                        var91 = -0.002444425_f64;
                    } else {
                        var91 = -0.020050623_f64;
                    }
                }
            }
        }
    } else {
        if input[19] < 387.07837_f64 {
            if input[20] < 21.302843_f64 {
                if input[0] < 2339.0_f64 {
                    var91 = 0.005695374_f64;
                } else {
                    var91 = -0.023064708_f64;
                }
            } else {
                if input[12] < 0.2320377_f64 {
                    if input[20] < 24.83409_f64 {
                        var91 = 0.012444864_f64;
                    } else {
                        var91 = -0.0018028703_f64;
                    }
                } else {
                    if input[35] < 17.880209_f64 {
                        var91 = -0.009588234_f64;
                    } else {
                        var91 = 0.006358452_f64;
                    }
                }
            }
        } else {
            if input[35] < 18.259357_f64 {
                if input[24] < 107337.0_f64 {
                    if input[10] < 0.29043126_f64 {
                        var91 = -0.0076762997_f64;
                    } else {
                        var91 = 0.007635839_f64;
                    }
                } else {
                    if input[13] < 0.38732994_f64 {
                        var91 = -0.0072940732_f64;
                    } else {
                        var91 = 0.009018166_f64;
                    }
                }
            } else {
                if input[10] < 0.13652053_f64 {
                    if input[22] < 7.400384_f64 {
                        var91 = -0.02185793_f64;
                    } else {
                        var91 = 0.004385968_f64;
                    }
                } else {
                    if input[1] < 5.2162094_f64 {
                        var91 = 0.010625758_f64;
                    } else {
                        var91 = 0.00031630966_f64;
                    }
                }
            }
        }
    }
    let var92: f64;
    if input[35] < 19.148708_f64 {
        if input[13] < 0.39241052_f64 {
            if input[10] < 0.24074075_f64 {
                if input[11] < 0.21397485_f64 {
                    if input[22] < 6.2262416_f64 {
                        var92 = 0.0020608534_f64;
                    } else {
                        var92 = 0.00054486_f64;
                    }
                } else {
                    if input[19] < 310.96075_f64 {
                        var92 = 0.0007771283_f64;
                    } else {
                        var92 = -0.0026839913_f64;
                    }
                }
            } else {
                if input[1] < 10.076003_f64 {
                    if input[6] < 115.0_f64 {
                        var92 = -0.00057461485_f64;
                    } else {
                        var92 = 0.0007819915_f64;
                    }
                } else {
                    if input[26] < 14.312945_f64 {
                        var92 = -0.019582622_f64;
                    } else {
                        var92 = -0.0016610635_f64;
                    }
                }
            }
        } else {
            if input[35] < 18.340254_f64 {
                if input[7] < 1212.0_f64 {
                    if input[6] < 2197.0_f64 {
                        var92 = 0.00006328298_f64;
                    } else {
                        var92 = -0.012822099_f64;
                    }
                } else {
                    if input[15] < 29.0_f64 {
                        var92 = -0.024072155_f64;
                    } else {
                        var92 = 0.0025836516_f64;
                    }
                }
            } else {
                if input[0] < 8511.0_f64 {
                    if input[35] < 18.604809_f64 {
                        var92 = -0.004916722_f64;
                    } else {
                        var92 = -0.04458287_f64;
                    }
                } else {
                    if input[3] < 5458.909_f64 {
                        var92 = 0.01913565_f64;
                    } else {
                        var92 = 0.0049981317_f64;
                    }
                }
            }
        }
    } else {
        if input[10] < 0.10353011_f64 {
            if input[1] < 7.476715_f64 {
                if input[26] < 31.340298_f64 {
                    if input[2] < 62.0_f64 {
                        var92 = -0.010960796_f64;
                    } else {
                        var92 = 0.013892921_f64;
                    }
                } else {
                    if input[11] < 0.22048691_f64 {
                        var92 = -0.022275837_f64;
                    } else {
                        var92 = 0.010694347_f64;
                    }
                }
            } else {
                if input[30] < 10.0_f64 {
                    if input[1] < 9.026796_f64 {
                        var92 = -0.0052951607_f64;
                    } else {
                        var92 = 0.019236518_f64;
                    }
                } else {
                    if input[3] < 4896.476_f64 {
                        var92 = -0.02224668_f64;
                    } else {
                        var92 = -0.002633184_f64;
                    }
                }
            }
        } else {
            if input[12] < 0.2680742_f64 {
                if input[26] < 6.327245_f64 {
                    if input[10] < 0.29183957_f64 {
                        var92 = 0.005758644_f64;
                    } else {
                        var92 = -0.0070948526_f64;
                    }
                } else {
                    if input[24] < 73801.0_f64 {
                        var92 = -0.0025045953_f64;
                    } else {
                        var92 = 0.000051106897_f64;
                    }
                }
            } else {
                if input[11] < 0.25368324_f64 {
                    if input[13] < 0.31385282_f64 {
                        var92 = -0.00019298475_f64;
                    } else {
                        var92 = 0.0037617825_f64;
                    }
                } else {
                    if input[11] < 0.25804585_f64 {
                        var92 = 0.01689358_f64;
                    } else {
                        var92 = 0.0041153114_f64;
                    }
                }
            }
        }
    }
    let var93: f64;
    if input[1] < 2.5747423_f64 {
        if input[13] < 0.30590808_f64 {
            if input[2] < 4.0_f64 {
                if input[35] < 19.44795_f64 {
                    if input[4] < 284.0_f64 {
                        var93 = -0.0035049233_f64;
                    } else {
                        var93 = -0.016487509_f64;
                    }
                } else {
                    if input[10] < 0.19215044_f64 {
                        var93 = 0.0053660567_f64;
                    } else {
                        var93 = 0.018941332_f64;
                    }
                }
            } else {
                if input[25] < 0.0024955638_f64 {
                    if input[7] < 839.0_f64 {
                        var93 = -0.03544649_f64;
                    } else {
                        var93 = -0.0022114129_f64;
                    }
                } else {
                    if input[5] < 258.0_f64 {
                        var93 = -0.01453603_f64;
                    } else {
                        var93 = 0.0030625141_f64;
                    }
                }
            }
        } else {
            if input[2] < 5.0_f64 {
                if input[7] < 1212.0_f64 {
                    if input[3] < 81.210526_f64 {
                        var93 = 0.002153693_f64;
                    } else {
                        var93 = -0.0034323551_f64;
                    }
                } else {
                    if input[11] < 0.1838843_f64 {
                        var93 = 0.016190996_f64;
                    } else {
                        var93 = 0.00051208556_f64;
                    }
                }
            } else {
                if input[35] < 17.74646_f64 {
                    if input[35] < 17.452911_f64 {
                        var93 = 0.0036465065_f64;
                    } else {
                        var93 = -0.0038143487_f64;
                    }
                } else {
                    if input[35] < 17.804674_f64 {
                        var93 = 0.012259276_f64;
                    } else {
                        var93 = 0.0031985273_f64;
                    }
                }
            }
        }
    } else {
        if input[1] < 3.0252814_f64 {
            if input[11] < 0.07709251_f64 {
                if input[26] < 10.362872_f64 {
                    if input[22] < 6.514544_f64 {
                        var93 = -0.010925803_f64;
                    } else {
                        var93 = 0.006964651_f64;
                    }
                } else {
                    if input[10] < 0.28774422_f64 {
                        var93 = -0.017235935_f64;
                    } else {
                        var93 = -0.063737914_f64;
                    }
                }
            } else {
                if input[13] < 0.41384995_f64 {
                    if input[4] < 5438.0_f64 {
                        var93 = -0.0010543084_f64;
                    } else {
                        var93 = 0.002683684_f64;
                    }
                } else {
                    if input[24] < 22290.0_f64 {
                        var93 = 0.0005824234_f64;
                    } else {
                        var93 = -0.011815329_f64;
                    }
                }
            }
        } else {
            if input[3] < 192.1_f64 {
                if input[5] < 256.0_f64 {
                    if input[29] < 233.0_f64 {
                        var93 = 0.0020851865_f64;
                    } else {
                        var93 = -0.02236184_f64;
                    }
                } else {
                    if input[17] < 1909.0_f64 {
                        var93 = 0.016775358_f64;
                    } else {
                        var93 = 0.0063869744_f64;
                    }
                }
            } else {
                if input[15] < 28.0_f64 {
                    if input[13] < 0.46285716_f64 {
                        var93 = 0.000033460576_f64;
                    } else {
                        var93 = -0.008003747_f64;
                    }
                } else {
                    if input[20] < 14.625984_f64 {
                        var93 = 0.0022955684_f64;
                    } else {
                        var93 = 0.0004738663_f64;
                    }
                }
            }
        }
    }
    let var94: f64;
    if input[15] < 43.0_f64 {
        if input[12] < 0.09598741_f64 {
            if input[15] < 20.0_f64 {
                if input[8] < 143.0_f64 {
                    if input[10] < 0.305761_f64 {
                        var94 = -0.0113972295_f64;
                    } else {
                        var94 = 0.0042786826_f64;
                    }
                } else {
                    if input[2] < 76.0_f64 {
                        var94 = -0.041865233_f64;
                    } else {
                        var94 = 0.018568419_f64;
                    }
                }
            } else {
                if input[22] < 3.9744623_f64 {
                    if input[2] < 47.0_f64 {
                        var94 = -0.0036793076_f64;
                    } else {
                        var94 = 0.017395288_f64;
                    }
                } else {
                    if input[22] < 4.3839293_f64 {
                        var94 = -0.00864376_f64;
                    } else {
                        var94 = -0.0008464527_f64;
                    }
                }
            }
        } else {
            if input[11] < 0.08375_f64 {
                if input[1] < 5.0221744_f64 {
                    if input[22] < 5.385421_f64 {
                        var94 = -0.000121512036_f64;
                    } else {
                        var94 = -0.009788029_f64;
                    }
                } else {
                    if input[24] < 27080.0_f64 {
                        var94 = -0.019233389_f64;
                    } else {
                        var94 = 0.0006967467_f64;
                    }
                }
            } else {
                if input[35] < 17.271885_f64 {
                    if input[10] < 0.29183957_f64 {
                        var94 = -0.00043913373_f64;
                    } else {
                        var94 = -0.009642005_f64;
                    }
                } else {
                    if input[11] < 0.20651747_f64 {
                        var94 = 0.0006776738_f64;
                    } else {
                        var94 = 0.00012585582_f64;
                    }
                }
            }
        }
    } else {
        if input[19] < 427.93463_f64 {
            if input[35] < 17.109346_f64 {
                if input[22] < 7.4495945_f64 {
                    var94 = -0.001225991_f64;
                } else {
                    if input[16] < 36.083652_f64 {
                        var94 = -0.019484311_f64;
                    } else {
                        var94 = -0.005287319_f64;
                    }
                }
            } else {
                if input[35] < 17.352804_f64 {
                    if input[16] < 38.44282_f64 {
                        var94 = 0.02215287_f64;
                    } else {
                        var94 = 0.004191346_f64;
                    }
                } else {
                    if input[16] < 38.120872_f64 {
                        var94 = -0.0014072711_f64;
                    } else {
                        var94 = 0.005447756_f64;
                    }
                }
            }
        } else {
            if input[24] < 120109.0_f64 {
                if input[4] < 4355.0_f64 {
                    if input[22] < 7.5069256_f64 {
                        var94 = 0.007646245_f64;
                    } else {
                        var94 = -0.0027781967_f64;
                    }
                } else {
                    if input[24] < 60908.0_f64 {
                        var94 = -0.03775423_f64;
                    } else {
                        var94 = -0.0025542525_f64;
                    }
                }
            } else {
                if input[4] < 11797.0_f64 {
                    if input[22] < 6.202124_f64 {
                        var94 = -0.031389166_f64;
                    } else {
                        var94 = 0.012423456_f64;
                    }
                } else {
                    if input[3] < 6346.6816_f64 {
                        var94 = 0.0010210125_f64;
                    } else {
                        var94 = -0.015012898_f64;
                    }
                }
            }
        }
    }
    let var95: f64;
    if input[30] < 10.0_f64 {
        if input[33] < 169076.0_f64 {
            if input[19] < 340.42465_f64 {
                if input[5] < 1474.0_f64 {
                    if input[11] < 0.102564104_f64 {
                        var95 = -0.0052324417_f64;
                    } else {
                        var95 = -0.00029554075_f64;
                    }
                } else {
                    if input[35] < 18.653639_f64 {
                        var95 = -0.015891235_f64;
                    } else {
                        var95 = 0.002455873_f64;
                    }
                }
            } else {
                if input[15] < 34.0_f64 {
                    var95 = -0.008648089_f64;
                } else {
                    var95 = -0.047545265_f64;
                }
            }
        } else {
            if input[4] < 10530.0_f64 {
                if input[19] < 304.4012_f64 {
                    var95 = -0.020852027_f64;
                } else {
                    if input[0] < 18475.0_f64 {
                        var95 = 0.01914517_f64;
                    } else {
                        var95 = -0.014601058_f64;
                    }
                }
            } else {
                if input[1] < 7.353603_f64 {
                    if input[0] < 11593.0_f64 {
                        var95 = -0.0073474734_f64;
                    } else {
                        var95 = -0.024680337_f64;
                    }
                } else {
                    if input[0] < 11593.0_f64 {
                        var95 = 0.0064185183_f64;
                    } else {
                        var95 = 0.00097083574_f64;
                    }
                }
            }
        }
    } else {
        if input[4] < 86.0_f64 {
            if input[29] < 87.0_f64 {
                if input[5] < 77.0_f64 {
                    if input[1] < 2.2915876_f64 {
                        var95 = -0.00025887263_f64;
                    } else {
                        var95 = 0.018203046_f64;
                    }
                } else {
                    if input[29] < 80.0_f64 {
                        var95 = -0.012664877_f64;
                    } else {
                        var95 = 0.00091868144_f64;
                    }
                }
            } else {
                if input[16] < 20.206203_f64 {
                    var95 = 0.02637515_f64;
                } else {
                    if input[16] < 20.416943_f64 {
                        var95 = -0.030476633_f64;
                    } else {
                        var95 = 0.006300745_f64;
                    }
                }
            }
        } else {
            if input[24] < 2467.0_f64 {
                if input[3] < 61.473682_f64 {
                    if input[20] < 12.012411_f64 {
                        var95 = -0.022708524_f64;
                    } else {
                        var95 = -0.00009959423_f64;
                    }
                } else {
                    if input[11] < 0.24220484_f64 {
                        var95 = -0.008266988_f64;
                    } else {
                        var95 = -0.037466742_f64;
                    }
                }
            } else {
                if input[3] < 81.210526_f64 {
                    if input[13] < 0.39587975_f64 {
                        var95 = 0.0077713663_f64;
                    } else {
                        var95 = 0.00016697391_f64;
                    }
                } else {
                    if input[24] < 3235.0_f64 {
                        var95 = -0.009282614_f64;
                    } else {
                        var95 = 0.00035945562_f64;
                    }
                }
            }
        }
    }
    let var96: f64;
    if input[10] < 0.35_f64 {
        if input[5] < 71.0_f64 {
            if input[17] < 751.0_f64 {
                if input[8] < 206.0_f64 {
                    if input[1] < 10.973457_f64 {
                        var96 = -0.00033278667_f64;
                    } else {
                        var96 = -0.008767712_f64;
                    }
                } else {
                    if input[7] < 87.0_f64 {
                        var96 = 0.0073820017_f64;
                    } else {
                        var96 = 0.023127351_f64;
                    }
                }
            } else {
                if input[3] < 4194.2856_f64 {
                    if input[3] < 3106.3635_f64 {
                        var96 = -0.005469844_f64;
                    } else {
                        var96 = 0.008603602_f64;
                    }
                } else {
                    if input[7] < 196.0_f64 {
                        var96 = -0.016444549_f64;
                    } else {
                        var96 = 0.011377596_f64;
                    }
                }
            }
        } else {
            if input[15] < 43.0_f64 {
                if input[22] < 8.324042_f64 {
                    if input[35] < 19.148708_f64 {
                        var96 = 0.00041058628_f64;
                    } else {
                        var96 = -0.00037073615_f64;
                    }
                } else {
                    if input[2] < 32.0_f64 {
                        var96 = 0.0057316055_f64;
                    } else {
                        var96 = -0.010353784_f64;
                    }
                }
            } else {
                if input[10] < 0.13791667_f64 {
                    if input[10] < 0.09416445_f64 {
                        var96 = 0.006942471_f64;
                    } else {
                        var96 = -0.005895553_f64;
                    }
                } else {
                    if input[4] < 15068.0_f64 {
                        var96 = 0.0031877276_f64;
                    } else {
                        var96 = -0.010674747_f64;
                    }
                }
            }
        }
    } else {
        if input[20] < 16.546991_f64 {
            if input[0] < 2159.0_f64 {
                if input[8] < 719.0_f64 {
                    if input[7] < 163.0_f64 {
                        var96 = -0.0017653358_f64;
                    } else {
                        var96 = 0.004851406_f64;
                    }
                } else {
                    if input[7] < 322.0_f64 {
                        var96 = -0.027998278_f64;
                    } else {
                        var96 = 0.008860778_f64;
                    }
                }
            } else {
                if input[7] < 413.0_f64 {
                    if input[8] < 1057.0_f64 {
                        var96 = 0.02296632_f64;
                    } else {
                        var96 = 0.0007956293_f64;
                    }
                } else {
                    if input[1] < 6.9273744_f64 {
                        var96 = 0.009265915_f64;
                    } else {
                        var96 = -0.007132642_f64;
                    }
                }
            }
        } else {
            if input[20] < 16.996424_f64 {
                if input[4] < 7850.0_f64 {
                    if input[1] < 6.4393086_f64 {
                        var96 = -0.011003942_f64;
                    } else {
                        var96 = 0.0051864446_f64;
                    }
                } else {
                    if input[7] < 131.0_f64 {
                        var96 = -0.007129211_f64;
                    } else {
                        var96 = -0.05285343_f64;
                    }
                }
            } else {
                if input[4] < 14003.0_f64 {
                    if input[13] < 0.3180723_f64 {
                        var96 = -0.006915256_f64;
                    } else {
                        var96 = -0.0003610409_f64;
                    }
                } else {
                    var96 = -0.035531256_f64;
                }
            }
        }
    }
    let var97: f64;
    if input[30] < 18.0_f64 {
        if input[22] < 6.178954_f64 {
            if input[15] < 28.0_f64 {
                if input[16] < 26.305569_f64 {
                    if input[22] < 5.404372_f64 {
                        var97 = 0.00043240676_f64;
                    } else {
                        var97 = -0.0016346779_f64;
                    }
                } else {
                    if input[13] < 0.44552845_f64 {
                        var97 = -0.0011658234_f64;
                    } else {
                        var97 = -0.014562815_f64;
                    }
                }
            } else {
                if input[16] < 31.591837_f64 {
                    if input[12] < 0.32611465_f64 {
                        var97 = 0.0009368904_f64;
                    } else {
                        var97 = 0.005686136_f64;
                    }
                } else {
                    if input[10] < 0.3643846_f64 {
                        var97 = -0.00000049545014_f64;
                    } else {
                        var97 = -0.010946437_f64;
                    }
                }
            }
        } else {
            if input[22] < 6.665479_f64 {
                if input[11] < 0.3506606_f64 {
                    if input[26] < 4.6979604_f64 {
                        var97 = 0.0028438836_f64;
                    } else {
                        var97 = -0.001560538_f64;
                    }
                } else {
                    if input[3] < 4690.636_f64 {
                        var97 = -0.0067169974_f64;
                    } else {
                        var97 = -0.038527098_f64;
                    }
                }
            } else {
                if input[5] < 95.0_f64 {
                    if input[20] < 16.606812_f64 {
                        var97 = -0.014233305_f64;
                    } else {
                        var97 = 0.0069109784_f64;
                    }
                } else {
                    if input[11] < 0.36167213_f64 {
                        var97 = 0.0005990855_f64;
                    } else {
                        var97 = 0.012638933_f64;
                    }
                }
            }
        }
    } else {
        if input[15] < 27.0_f64 {
            if input[2] < 96.0_f64 {
                if input[19] < 124.3672_f64 {
                    if input[16] < 25.600283_f64 {
                        var97 = 0.0023184065_f64;
                    } else {
                        var97 = 0.0077070394_f64;
                    }
                } else {
                    if input[5] < 227.0_f64 {
                        var97 = 0.0024854154_f64;
                    } else {
                        var97 = -0.024843043_f64;
                    }
                }
            } else {
                if input[6] < 71.0_f64 {
                    var97 = -0.041268643_f64;
                } else {
                    if input[24] < 98016.0_f64 {
                        var97 = 0.006853433_f64;
                    } else {
                        var97 = -0.01111571_f64;
                    }
                }
            }
        } else {
            if input[1] < 6.83554_f64 {
                if input[1] < 6.12425_f64 {
                    if input[1] < 6.0992475_f64 {
                        var97 = 0.00066925655_f64;
                    } else {
                        var97 = -0.009509376_f64;
                    }
                } else {
                    if input[11] < 0.16968215_f64 {
                        var97 = -0.00069369737_f64;
                    } else {
                        var97 = 0.0041944445_f64;
                    }
                }
            } else {
                if input[4] < 3781.0_f64 {
                    if input[3] < 546.9_f64 {
                        var97 = -0.03391407_f64;
                    } else {
                        var97 = 0.002732897_f64;
                    }
                } else {
                    if input[24] < 64572.0_f64 {
                        var97 = -0.0029568253_f64;
                    } else {
                        var97 = 0.00008464236_f64;
                    }
                }
            }
        }
    }
    let var98: f64;
    if input[10] < 0.10747664_f64 {
        if input[26] < 170.85095_f64 {
            if input[2] < 18.0_f64 {
                if input[4] < 2565.0_f64 {
                    if input[11] < 0.33568075_f64 {
                        var98 = -0.0032155798_f64;
                    } else {
                        var98 = -0.018521024_f64;
                    }
                } else {
                    if input[7] < 1020.0_f64 {
                        var98 = -0.037828922_f64;
                    } else {
                        var98 = -0.0019697528_f64;
                    }
                }
            } else {
                if input[1] < 7.1251564_f64 {
                    if input[13] < 0.45728898_f64 {
                        var98 = 0.0015409611_f64;
                    } else {
                        var98 = 0.01686742_f64;
                    }
                } else {
                    if input[1] < 10.697594_f64 {
                        var98 = -0.0042793937_f64;
                    } else {
                        var98 = 0.006349602_f64;
                    }
                }
            }
        } else {
            if input[5] < 61.0_f64 {
                if input[24] < 105175.0_f64 {
                    if input[3] < 4004.8096_f64 {
                        var98 = -0.0047646775_f64;
                    } else {
                        var98 = -0.03416821_f64;
                    }
                } else {
                    if input[7] < 127.0_f64 {
                        var98 = -0.0024216403_f64;
                    } else {
                        var98 = 0.01431379_f64;
                    }
                }
            } else {
                if input[1] < 4.9770117_f64 {
                    var98 = -0.008309204_f64;
                } else {
                    var98 = -0.05037273_f64;
                }
            }
        }
    } else {
        if input[2] < 10.0_f64 {
            if input[24] < 16390.0_f64 {
                if input[3] < 455.15_f64 {
                    if input[10] < 0.31768888_f64 {
                        var98 = 0.0012645635_f64;
                    } else {
                        var98 = -0.0047126873_f64;
                    }
                } else {
                    if input[4] < 898.0_f64 {
                        var98 = -0.03393248_f64;
                    } else {
                        var98 = -0.0072795227_f64;
                    }
                }
            } else {
                if input[35] < 17.159575_f64 {
                    if input[10] < 0.24722503_f64 {
                        var98 = 0.0011855616_f64;
                    } else {
                        var98 = -0.03477326_f64;
                    }
                } else {
                    if input[13] < 0.36757424_f64 {
                        var98 = 0.001829722_f64;
                    } else {
                        var98 = 0.00792297_f64;
                    }
                }
            }
        } else {
            if input[15] < 20.0_f64 {
                if input[25] < 0.04212845_f64 {
                    var98 = -0.042395484_f64;
                } else {
                    if input[24] < 152717.0_f64 {
                        var98 = -0.0014178213_f64;
                    } else {
                        var98 = 0.014525281_f64;
                    }
                }
            } else {
                if input[11] < 0.08375_f64 {
                    if input[1] < 3.550686_f64 {
                        var98 = -0.017137898_f64;
                    } else {
                        var98 = -0.0011412501_f64;
                    }
                } else {
                    if input[12] < 0.28401726_f64 {
                        var98 = 0.00018698332_f64;
                    } else {
                        var98 = 0.0012327794_f64;
                    }
                }
            }
        }
    }
    let var99: f64;
    if input[13] < 0.46285716_f64 {
        if input[30] < 10.0_f64 {
            if input[35] < 20.16387_f64 {
                if input[3] < 6042.5454_f64 {
                    if input[2] < 97.0_f64 {
                        var99 = -0.0005585203_f64;
                    } else {
                        var99 = 0.0053752544_f64;
                    }
                } else {
                    if input[16] < 18.382183_f64 {
                        var99 = 0.011587106_f64;
                    } else {
                        var99 = -0.0071723456_f64;
                    }
                }
            } else {
                if input[1] < 3.8153753_f64 {
                    var99 = 0.0032752554_f64;
                } else {
                    if input[1] < 7.1251564_f64 {
                        var99 = -0.012794304_f64;
                    } else {
                        var99 = -0.033190854_f64;
                    }
                }
            }
        } else {
            if input[15] < 45.0_f64 {
                if input[13] < 0.2934363_f64 {
                    if input[4] < 13240.0_f64 {
                        var99 = -0.0015374554_f64;
                    } else {
                        var99 = 0.010824945_f64;
                    }
                } else {
                    if input[10] < 0.15306123_f64 {
                        var99 = -0.0003509959_f64;
                    } else {
                        var99 = 0.00039656094_f64;
                    }
                }
            } else {
                if input[19] < 387.07837_f64 {
                    if input[20] < 21.302843_f64 {
                        var99 = -0.008509403_f64;
                    } else {
                        var99 = 0.0077974196_f64;
                    }
                } else {
                    if input[35] < 18.259357_f64 {
                        var99 = -0.0022068447_f64;
                    } else {
                        var99 = 0.003994007_f64;
                    }
                }
            }
        }
    } else {
        if input[29] < 122.0_f64 {
            if input[22] < 5.648443_f64 {
                if input[2] < 86.0_f64 {
                    if input[8] < 395.0_f64 {
                        var99 = -0.0041335053_f64;
                    } else {
                        var99 = 0.013362937_f64;
                    }
                } else {
                    if input[35] < 16.951084_f64 {
                        var99 = -0.0076682414_f64;
                    } else {
                        var99 = -0.03191427_f64;
                    }
                }
            } else {
                if input[10] < 0.17613636_f64 {
                    if input[22] < 6.6296387_f64 {
                        var99 = -0.032067284_f64;
                    } else {
                        var99 = -0.011230908_f64;
                    }
                } else {
                    var99 = 0.00067901716_f64;
                }
            }
        } else {
            if input[11] < 0.27228683_f64 {
                if input[24] < 117219.0_f64 {
                    if input[24] < 94796.0_f64 {
                        var99 = -0.0022370631_f64;
                    } else {
                        var99 = 0.0065777185_f64;
                    }
                } else {
                    if input[24] < 127044.0_f64 {
                        var99 = -0.025028495_f64;
                    } else {
                        var99 = -0.002339313_f64;
                    }
                }
            } else {
                if input[10] < 0.13217391_f64 {
                    if input[2] < 72.0_f64 {
                        var99 = 0.028194537_f64;
                    } else {
                        var99 = 0.012764891_f64;
                    }
                } else {
                    var99 = -0.009176031_f64;
                }
            }
        }
    }
    nan_f64 + (var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + var25 + var26 + var27 + var28 + var29 + var30 + var31 + var32 + var33 + var34 + var35 + var36 + var37 + var38 + var39 + var40 + var41 + var42 + var43 + var44 + var45 + var46 + var47 + var48 + var49 + var50 + var51 + var52 + var53 + var54 + var55 + var56 + var57 + var58 + var59 + var60 + var61 + var62 + var63 + var64 + var65 + var66 + var67 + var68 + var69 + var70 + var71 + var72 + var73 + var74 + var75 + var76 + var77 + var78 + var79 + var80 + var81 + var82 + var83 + var84 + var85 + var86 + var87 + var88 + var89 + var90 + var91 + var92 + var93 + var94 + var95 + var96 + var97 + var98 + var99)
}
