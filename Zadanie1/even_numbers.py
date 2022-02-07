import random


class EvenNumber:

    def create_list_of_numbers(self, list_size):
        created_numbers = []
        i = 0
        while i < list_size:
            number = random.randint(1, 100)      # just for our case I decided that we will have values from 1 to 100 :)
            created_numbers.append(number)
            i += 1
        return created_numbers

    def choose_even_numbers_only(self, created_numbers):
        even_numbers = []
        for i in created_numbers:
            if i % 2 == 0:
                even_numbers.append(i)
            else:
                continue
        return even_numbers
