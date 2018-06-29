import sys 

class Player(object):
    def __init__(self, stars=0, rank=25):
        self.stars = stars
        self.rank = rank
        self.row_wins = 0
        self.legend_status = False
        self.STARS = {1:5,2:5,3:5,4:5,5:5,6:5,7:5,8:5,9:5,10:5,11:4,12:4,13:4,
                        14:4,15:4,16:3,17:3,18:3,19:3,20:3,21:2,22:2,23:2,
                        24:2,25:2}

    def win(self):
        gained_stars = 0
        self.row_wins +=1
        if self.legend_status:
            return  
        if self.row_wins >= 3 and 6<=self.rank<=25:
            gained_stars = 2
        else:
            gained_stars = 1
        self.level_up(gained=gained_stars)

    def lose(self):
        lost_stars = 0
        self.row_wins=0
        if self.legend_status:
            return
        if 1<=self.rank<=20:
            lost_stars = 1
        self.level_up(lost=lost_stars)

    def level_up(self, lost=0, gained=0):
        if gained is not 0:
            self.stars += gained
            if self.rank==1 and self.stars>5:
                self.legend_status=True
            if self.stars > self.STARS[self.rank]:
                self.stars-= self.STARS[self.rank]
                self.rank-=1 
        if lost is not 0:
            if self.rank<20:
                self.stars-=1
                if self.stars == 1:
                    self.rank+=1
                    self.stars = self.STARS[self.rank]-1

    def __str__(self):
        if self.legend_status:
            return 'Legend'
        return str(self.rank)

if __name__ == "__main__":
    string = sys.stdin.read().strip()
    if len(string)>10000:
        raise Exception('String input cannot be longer than 10,000')
    player = Player()
    for char in string.lower():
        if char=='w':
            player.win()
        elif char=='l':
            player.lose()
        else:
            raise Exception('Invalid Character entered')
    print(player)