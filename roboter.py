# coding: utf-8
'''
udemy python intro
-> roboter application
'''
import csv
from collections import OrderedDict


class Robot():
    '''
    this class is Robot class
    '''
    def __init__(self, my_name):
        self.my_name = my_name

    def say_what_your_name(self):
        '''
        do question -> what your name
        '''
        print("Hello! I'm {}.".format(self.my_name))
        print('What your name?')

    def which_like(self, person_name):
        '''
        do question -> while restaurant do you like?
        '''
        self.person_name = person_name
        print('Mr. {}.Which restaurant do you like?'.format(self.person_name))

    def say_good_bye(self):
        '''
        say good bye
        '''
        print('Mr. {}.Thank you.'.format(self.person_name))
        print('Have a nice day! good bye.')

    def say_recommend(self):
        '''
        This function recommends all the most restaurants
        '''
        fieldnames = ['Name', 'Count']
        with open('ranking.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            restaurant_list = [row for row in reader]
        if not restaurant_list:
            pass
        else:
            max_count = int(restaurant_list[0]['Count'])
            print(max_count)
            for i in range(len(restaurant_list)):
                restaurant_list[i]['Count'] = int(restaurant_list[i]['Count'])
                if restaurant_list[i]['Count'] == max_count:
                    print('I recommend this {}.'.format(restaurant_list[i]['Name']))
                    print('Are you like?[Yes/No]')
                    yes_or_no = input()
                    if yes_or_no == 'Yes' or yes_or_no == 'yes':
                        restaurant_list[i]['Count'] += 1
                    else:
                        continue
            restaurant_list.sort(key=lambda x: x['Count'], reverse=True)
            with open('ranking.csv', 'w') as csv_file:
                fieldnames = ['Name', 'Count']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(restaurant_list)


class Ranking():
    '''
    This class has all ability to operate ranking.csv
    '''
    def __init__(self, like_restaurant=None):
        self.like_restaurant = like_restaurant
        self.count = None

    def add_restaurant(self):
        '''
        add new restaurant to ranking.csv
        sorted restaurant by 'Count'
        '''
        restaurant_list = self._read_restaurant()
        check = 0
        for i in range(len(restaurant_list)):
            restaurant_list[i]['Count'] = int(restaurant_list[i]['Count'])
            if restaurant_list[i]['Name'] == self.like_restaurant:
                restaurant_list[i]['Count'] += 1
                check = 1
            else:
                continue
        if check == 0:
            restaurant_list.append(OrderedDict([('Name', self.like_restaurant),
                                                ('Count', 1)]))
        else:
            restaurant_list = sorted(restaurant_list, key=lambda x: x['Count'],
                                     reverse=True)
        with open('ranking.csv', 'w') as csv_file:
            fieldnames = ['Name', 'Count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(restaurant_list)

    def _read_restaurant(self):
        '''
        private function
        read ranking.csv
        '''
        with open('ranking.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            restaurant_list = [row for row in reader]
        return restaurant_list


def main():
    '''
    main function
    '''
    while 1:
        robot = Robot(roboko)
        robot.say_what_your_name()
        person_name = input()
        robot.say_recommend()
        robot.which_like(person_name)
        restaurant = input().title()
        ranking = Ranking(restaurant)
        ranking.add_restaurant()
        robot.say_good_bye()

if __name__ == '__main__':
    roboko = 'Roboko'
    main()
