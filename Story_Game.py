def Story_Game():
    a = input('Enter a place: (Park,Zoo)')
    b = input('Enter an adjective: (a,an)')
    c = input('Enter a noun : (monkey,rabbit)')
    d = input('Enter a verb(past tense) (was,were): ')
    e = input('Enter another noun (hand, mouth):')
    g = input('Enter another noun (banana,carrot): ')
    i = input('Enter another pronoun (friend): ')

    Story = f'''Today I went to the {a}. I saw a {b} {c} jumping up and down in a tree. He {d} through the large tunnel that led to its {e}. I got some {g} and fed it to the {c} to make it {i}.
'''
    
    print(Story)


if __name__=="__main__":
    Story_Game()
    