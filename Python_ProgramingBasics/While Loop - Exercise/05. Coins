money = float(input())


two_leva = 0
one_leva = 0
fifty_stotinki = 0
twenty_stotinki = 0
ten_stotinki = 0
five_stotinki = 0
two_stotinki = 0
one_stotinki = 0


while money > 0:
    if money // 2 != 0:
        two_leva = money // 2
        money -= 2 * two_leva
    elif money // 1 != 0:
        one_leva = money // 1
        money -= 1 * one_leva
    elif money // 0.5 != 0:
        fifty_stotinki = money // 0.5
        money -= 0.5 * fifty_stotinki
    elif money // 0.2 != 0:
        twenty_stotinki = money // 0.2
        money -= 0.2 * twenty_stotinki
    elif money // 0.1 != 0:
        ten_stotinki = money // 0.1
        money -= 0.1 * ten_stotinki
    elif money // 0.05 != 0:
        five_stotinki = money // 0.05
        money -= 0.05 * five_stotinki
    elif money // 0.02 != 0:
        two_stotinki = money // 0.02
        money -= 0.02 * two_stotinki
    elif money // 0.01 != 0:
        one_stotinki = money // 0.01
        money -= 0.01 * one_stotinki

    money = round(money, 2)

coin_count = (two_leva + one_leva + fifty_stotinki + twenty_stotinki
              + ten_stotinki + five_stotinki + two_stotinki + one_stotinki)

print(int(coin_count))
