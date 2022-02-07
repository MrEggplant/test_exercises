from even_numbers import EvenNumber


if __name__ == '__main__':
    list_size = int(input("How long is your list with numbers? Please type the value: "))

    my_list = EvenNumber()
    entered_numbers = my_list.create_list_of_numbers(list_size)
    print(entered_numbers)

    my_results = EvenNumber()
    my_results = my_results.choose_even_numbers_only(entered_numbers)
    print(my_results)
