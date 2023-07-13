import fileinput

grammar = []

for line in fileinput.input():
    grammar += line.strip().split("\n")


# if the grammar is only one rule, we can definitively state what the final state is
if len(grammar) == 1:
    for line in grammar:
        transition = line.split()
        current_state = transition[0]
        consumed = transition[1]

        # rule ends in terminal or epsilon
        final_state = current_state
        print(final_state)
        if len(transition) == 2:
            if consumed == "*e*":
                print('(' + current_state + ' (' + current_state + " " + consumed + '))')
            else:
                print('(' + current_state + ' (' + current_state + " \"" + consumed + '\"))')
        # rule ends in NT and terminal
        else:
            final_state = transition[2]
            print(final_state)
            if consumed == "*e*":
                print('(' + current_state + ' (' + end_state + " " + consumed + '))')
            else:
                print('(' + current_state + ' (' + end_state + " \"" + consumed + '\"))')

# if the grammar is more than one rule long, it is harder to accommodate all potential final states -
# for carmel-formatting; thus, every rule that ends in a single terminal/epsilon goes to a new final state "FIN"
else:
    print('FIN')
    for line in grammar:
        transition = line.split()
        current_state = transition[0]
        destination_state = ''
        consumed = transition[1]

        # rule ends in terminal or epsilon
        if len(transition) == 2:
            destination_state = 'FIN'
            if consumed == "*e*":
                print('(' + current_state + ' (' + destination_state + " " + consumed + '))')
            else:
                print('(' + current_state + ' (' + destination_state + " \"" + consumed + '\"))')
        # rule ends in NT and terminal
        else:
            destination_state = transition[2]
            if consumed == "*e*":
                print('(' + current_state + ' (' + destination_state + " " + consumed + '))')
            else:
                print('(' + current_state + ' (' + destination_state + " \"" + consumed + '\"))')
