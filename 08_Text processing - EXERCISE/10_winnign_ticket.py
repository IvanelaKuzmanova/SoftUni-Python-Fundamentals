def ticket_check(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols_list = ['@', '#', '$', '^']
    left_part = ticket[:10]        #to index 10 since valid tickets are 20 chars long
    right_part = ticket[10:]

    for current_symbol in winning_symbols_list:
        for uninterrupted_match in range(10, 5, -1):        #to check each half
            winning_symbol_repeat = current_symbol * uninterrupted_match
            if winning_symbol_repeat in left_part and winning_symbol_repeat in right_part:      #winning ticket
                if uninterrupted_match == 10:       #jackpot
                    return f'ticket "{ticket}" - {uninterrupted_match}{current_symbol} Jackpot!'

                #just winning ticket but not jackpot
                return f'ticket "{ticket}" - {uninterrupted_match}{current_symbol}'

    return f'ticket "{ticket}" - no match'


tickets_list = [ticket.strip() for ticket in input().split(", ")]        #strip to remove intervals

for current_ticket in tickets_list:
    print(ticket_check(current_ticket))