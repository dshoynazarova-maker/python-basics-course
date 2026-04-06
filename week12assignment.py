data ='''PixelPlay,Gaming,800,500
ChefAnna,Cooking,1200,1000
GuitarGuy,Music,500,200
SpeedRun,Gaming,1500,1000
Broken,Row,No,Cash
TastyTreats,Cooking,300,100
ProGamer,Gaming,2000,3000'''
#ChannelName,Category,AdRevenue,SubRevenue

with open("streamer_income.txt", "w") as file:
    file.write(data)

def calculate_streamer_earnings(file1):
    with open('streamer_income.txt','r') as file1:
        category_totals = {}
        top_earners = []
        for line in file1:
            new_line = line.strip().split(',')
            channel_name = str(new_line[0])
            category = str(new_line[1])
            try:
                adrevenue = int(new_line[2])
                subrevenue = int(new_line[3])
                total_earnings = adrevenue + subrevenue
                if category in category_totals:
                    category_totals[category] += total_earnings
                else:
                    category_totals[category] = total_earnings
                if total_earnings > 2000:
                    top_earners.append((channel_name,total_earnings))
            except ValueError:
                continue
    return category_totals , top_earners
def generate_income_statement(category_totals, top_earners):
    with open('income_statement.txt','w') as file2:
        file2.write("REVENUE BY CATEGORY\n")
        file2.write("-------------------\n")
        for category,total in category_totals.items():
            file2.write(f'{category}: ${total:.2f}\n')
        file2.write('\nTOP EARNERS (> $2000)\n')
        file2.write('---------------------\n')
        for name, earnings in top_earners:
            file2.write(f'{name} (${earnings:.2f})\n')

category_totals, top_earners = calculate_streamer_earnings("streamer_income.txt")
generate_income_statement(category_totals, top_earners)

        



            



     