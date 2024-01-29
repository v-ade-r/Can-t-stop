import numpy as np
import statistics
import itertools
import pandas as pd
import time
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 800)

"""Can't Stop optimizer"""

'''1. Creating the structure and constraints - only for manual tests'''
# total = 0
# two = 0     #3max
# three = 0   #5max
# four = 1    #7max
# five = 0    #9max
# six = 0     #11max
# seven = 1   #13max
# eight = 1   #11max
# nine = 0    #9max
# ten = 0     #7max
# eleven = 0  #5max
# twelve = 0  #3max
#
# line1 = 10
# line2 = 8
# line3 = 6
#
# lines = {2 : 0,
#          3 : 0,
#          4 : 1,
#          5 : 0,
#          6 : 0,
#          7 : 1,
#          8 : 1,
#          9 : 0,
#          10 : 0,
#          11 : 0,
#          12 : 0}

'''2. Rolling 4 K6 dices and getting results'''
def k6x4_roll():
    x1 = np.random.randint(1, 7)
    x2 = np.random.randint(1, 7)
    x3 = np.random.randint(1, 7)
    x4 = np.random.randint(1, 7)

    y1 = [x1+x2, x3+x4]
    y2 = [x1+x3, x2+x4]
    y3 = [x1+x4, x2+x3]
    # print (x1,x2,x3,x4,
    #        y1,y2,y3)
    #
    # print('rolls: ',x1,x2,x3,x4 )
    return y1,y2,y3


'''3. 3line testing'''
def choices_after_roll(line1,line2,line3,lines):
    '''No line is chosen yet'''
    # print('lines w choices_after_roll: ', line1, line2, line3)

    while True:
        choice1 = []
        choice2 = []
        choice3 = []
        choice4 = []
        choice5 = []
        choice6 = []
        choice_number = 0

        rolls = k6x4_roll()

        '''checking if lines are available'''
        for para in rolls:
            choice_number += 1

            for j in range(len(para)):
                #print(para[j])
                #print(lines.get(para[j]))
                line_level = lines.get(para[j])
                if line_level != 'max':                 #checking if line is not finished
                    if line1 == 0 or line2 == 0 or line3 == 0 or line1 == para[j] or line2 == para[j] or line3 == para[j]:
                        '''checking if sum of 2 dices can match an occupied line or can be chosen because we haven't chosen all
                        3 lines yet'''
                        # print('j: ',j,'line1: ',line1, 'line2: ', line2, 'tested number: ', para[j], 'choice_number przed if: ', choice_number)
                        if j == 1 and line3 == 0 and line1 != 0 and line2 != 0 and line1 != para[j] and line2 != para[j]:
                            # print('choice1: ', choice1, 'line1: ',line1,  'choice2: ', choice2,'line2: ',line2,
                            #       'choice3: ', choice3, 'line3: ',line3, 'choice_number: ', choice_number)
                            if choice_number == 1 and (choice1 == [line1] or choice1 == [line2]):
                                choice1.append(para[j])
                                # print('1')
                            if choice_number == 1 and choice1[0] != line1 and choice1[0] != line2:
                                choice4.append(para[j])
                                # print('2')
                            if choice_number == 2 and (choice2 == [line1] or choice2 == [line2]):
                                choice2.append(para[j])
                                # print('3')
                            if choice_number == 2 and choice2[0] != line1 and choice2[0] != line2:
                                choice5.append(para[j])
                                # print('4')
                            if choice_number == 3 and (choice3 == [line1] or choice3 == [line2]):
                                choice3.append(para[j])
                                # print('5')
                            if choice_number == 3 and choice3[0] != line1 and choice3[0] != line2:
                                choice6.append(para[j])
                                # print('6')
                        else:
                            if choice_number == 1:
                                choice1.append(para[j])
                            if choice_number == 2:
                                choice2.append(para[j])
                            if choice_number == 3:
                                choice3.append(para[j])

                j += 1

        if not choice1:
            choice1.append('not possible')
        if not choice2:
            choice2.append('not possible')
        if not choice3:
            choice3.append('not possible')

        #print(choice1,choice2, choice3)

        break
    return choice1,choice2,choice3,choice4,choice5,choice6


def one_turn(line1,line2,line3,lines,total,number_of_rolls):

    proof = 0
    number_of_rolls += 1

    choices = choices_after_roll(line1,line2,line3,lines)
    choices = [x for x in choices if x != []]
    number_of_choices = len(choices)
    #print('number of choices: ',number_of_choices)

    if choices[0] == ['not possible'] and choices[1] == ['not possible'] and choices[2] == ['not possible']:
        return proof,total,line1,line2,line3,lines,number_of_rolls
    # print('choices: ', choices)
    # print(lines)
    # print('Choose your move. Choose option 1,2,3,4,5,6 (if possible)')
    choices = [x for x in choices if not x == ['not possible']]
    number_of_choices = len(choices)
    # print('number of choices: ', number_of_choices)
    # print('choices_after_strip: ', choices)

    while True:
        #choosing 1st,2nd or 3rd option
        #choice = int(input())
        while True:
            mark = 1
            choice = np.random.randint(1,number_of_choices+1)
            #print('choice: ',choice)
            for i in range(number_of_choices):
                if len(choices[choice-1]) < len(choices[i]):
                    mark = 0
                    continue
            if mark == 1:
                break

        if choice <= number_of_choices:
            #print('pysznie')
            break
        else:
            print('press a viable number you MORON')
            continue

    for chosen in choices[(choice - 1)]:
        first_on_the_line = False
        if lines[chosen] == 'max':
            break
        lines[chosen] += 1

        if line1 == 0 and line2 != chosen and line3 != chosen :
            line1 = chosen
            first_on_the_line = True
        if line1 != 0 and line1 != chosen and line2 == 0 and line3 != chosen:
            line2 = chosen
            first_on_the_line = True
        if line1 != 0 and line1 != chosen and line2 != chosen and line2 != 0 and line3 == 0:
            line3 = chosen
            first_on_the_line = True

        #print('lines w one_turn: ',line1, line2, line3)

        # useful for manual play, not so much for automatic odds testing
        '''if lines[2] == 3:
            lines[2] = 'max'
        if lines[3] == 5:
            lines[3] = 'max'
        if lines[4] == 7:
            lines[4] = 'max'
        if lines[5] == 9:
            lines[5] = 'max'
        if lines[6] == 11:
            lines[6] = 'max'
        if lines[7] == 13:
            lines[7] = 'max'
        if lines[8] == 11:
            lines[8] = 'max'
        if lines[9] == 9:
            lines[9] = 'max'
        if lines[10] == 7:
            lines[10] = 'max'
        if lines[11] == 5:
            lines[11] = 'max'
        if lines[12] == 3:
            lines[12] = 'max' '''

        if chosen == 2 or chosen == 12:
            total += 6
            if first_on_the_line:
                total += 6
        if chosen == 3 or chosen == 11:
            total += 5
            if first_on_the_line:
                total += 5
        if chosen == 4 or chosen == 10:
            total += 4
            if first_on_the_line:
                total += 4
        if chosen == 5 or chosen == 9:
            total += 3
            if first_on_the_line:
                total += 3
        if chosen == 6 or chosen == 8:
            total += 2
            if first_on_the_line:
                total += 2
        if chosen == 7:
            total += 1
            if first_on_the_line:
                total += 1

    #print(lines)
    proof = 1
    return proof,total,line1,line2,line3,lines,number_of_rolls

def one_round(line1_number,line2_number,line3_number,lines):
    line1 = line1_number
    line2 = line2_number
    line3 = line3_number
    lines = lines

    victory = 0
    total = 0
    number_of_rolls = 0
    game_on = 1

    while game_on > 0:
        game_on,total,line1,line2,line3,lines,number_of_rolls = one_turn(line1,line2,line3,lines,total,number_of_rolls)
        #print('total: ', total)
        sum_of_maxs = sum(value == 'max' for value in lines.values())
        '''if sum_of_maxs >= 1 and game_on == 1:
            print('Rozpierdoliłeś w drzazgi ziom!')
            victory = 1
            break
        if game_on < 1:
            print('Zjebałeś Spock')'''
    #print(lines)
    return total,number_of_rolls,victory

def optimal_average_total_limit_for_particular_3lines (line1_number,line2_number,line3_number):
    totals =[]
    numbers_of_rolls = []
    victories = []

    for i in range(1,100000):
        lines = {2: 0,
                 3: 0,
                 4: 0,
                 5: 0,
                 6: 0,
                 7: 0,
                 8: 0,
                 9: 0,
                 10: 0,
                 11: 0,
                 12: 0}

        for number in (line1_number, line2_number, line3_number):
            lines[number] += 1

        #print('lines after implying parameters: ', lines)

        total, number_of_rolls, victory = one_round(line1_number,line2_number,line3_number,lines)
        totals.append(total)
        numbers_of_rolls.append(number_of_rolls-1)
        victories.append(victory)
        i += 1

    average_total = statistics.median(totals)
    average_numbers_of_rolls = statistics.median(numbers_of_rolls)
    probability_of_finishing_one_line = statistics.median(victories)
    # print(totals,'\n',average_total)

    return average_total, average_numbers_of_rolls, probability_of_finishing_one_line


def whole_analysis_for_every_possible_3lines_combination():
    """This function returns data frame with a few columns, but the most important one is 'Rounded rolls' - which is
    actually the median value of number of rolls before the situation where next move is not possible, because k6x4 rolls
    don't give you the needed sum for any of your 3 lines. This value is calculated for every 3line combination"""

    all_possible_3lines_combinations = []
    all_lines = [2,3,4,5,6,7,8,9,10,11,12]
    all_possible_3lines_combinations.extend(itertools.combinations(all_lines,3))

    '''lists for collecting all the data before creating DataFrame: '''
    L_three_lines = []
    L_points_for_starting_specific_three_lines = []
    L_average_total = []
    L_average_total_plus_starting_points = []
    L_average_number_of_rolls = []
    L_average_rounded_number_of_rolls = []
    L_probability_of_finishing_one_line = []

    for three_lines in all_possible_3lines_combinations:
        points_for_starting_specific_three_lines = 0

        for i in range(len(three_lines)):
            if three_lines[i] == 2 or three_lines[i] == 12:
                points_for_starting_specific_three_lines += 12
            if three_lines[i] == 3 or three_lines[i] == 11:
                points_for_starting_specific_three_lines += 10
            if three_lines[i] == 4 or three_lines[i] == 10:
                points_for_starting_specific_three_lines += 8
            if three_lines[i] == 5 or three_lines[i] == 9:
                points_for_starting_specific_three_lines += 6
            if three_lines[i] == 6 or three_lines[i] == 8:
                points_for_starting_specific_three_lines += 4
            if three_lines[i] == 7:
                points_for_starting_specific_three_lines += 2

        average_total, average_number_of_rolls, probability_of_finishing_one_line = (
            optimal_average_total_limit_for_particular_3lines(three_lines[0], three_lines[1], three_lines[2]))

        average_total_plus_starting_points = average_total + points_for_starting_specific_three_lines

        L_three_lines.append(three_lines)
        L_points_for_starting_specific_three_lines.append(points_for_starting_specific_three_lines)
        L_average_total.append(average_total)
        L_average_total_plus_starting_points.append(average_total_plus_starting_points)
        L_average_number_of_rolls.append(average_number_of_rolls)
        L_average_rounded_number_of_rolls.append(round(average_number_of_rolls))
        L_probability_of_finishing_one_line.append(probability_of_finishing_one_line)

    data = pd.DataFrame({ '3 lines' : pd.Series(L_three_lines),
                          'Points for starting specific three lines' : pd.Series(L_points_for_starting_specific_three_lines),
                          'Average total' : pd.Series(L_average_total),
                          'Average total + starting points' : pd.Series((L_average_total_plus_starting_points)),
                          "Avg nr of rolls" : pd.Series(L_average_number_of_rolls),
                          "Rounded rolls" : pd.Series(L_average_rounded_number_of_rolls),
                          'Probability of finishing line' : pd.Series(L_probability_of_finishing_one_line)
                          })
    #print(data.sort_values(by='Average total + starting points', ascending=False))
    print(data[['3 lines',"Rounded rolls","Avg nr of rolls",'Average total']])
    return data


full_data = whole_analysis_for_every_possible_3lines_combination()

full_data = full_data.loc[:, ['3 lines', 'Rounded rolls', 'Avg nr of rolls']]
full_data = full_data.sort_values(by='Rounded rolls')
full_data.to_csv('cantstop.txt')

"""
Finally we got median for each 3line combination.

Next step should involve calculating expected value of rolls especially around the median number threshold to examine
if next roll is EV+ and we should continue or EV- and we should stop. In reality it's a complicated matter taking into
account position on the line, game state, opponents tendencies (looseness or tightness). 

I am not even sure if I need that. Right now I use these median values as a rule of thumb and correct them using my
knowledge and experience."""






