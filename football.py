import math
import random




class Playoff(object):
    def __init__(self, teams):
        self.teams = teams[:]
        self.MIN = 0
        self.MAX = 31
        self.tours = round(math.log(len(teams), 2))
        self.history = {tour: [] for tour in range(self.tours)}


    def _group(self, teams, by):
        """Случайно группирует команды"""

        temp_list_teams = teams[:]
        random.shuffle(temp_list_teams)
        
        return zip(*[iter(temp_list_teams)] * by)


    def _play_match(self, A, B):
        """Выявляет победителя матча"""

        number_of_goals = lambda team: random.randint(self.MIN, self.MAX)

        goals_team_A = number_of_goals(A)
        goals_team_B = number_of_goals(B)

        if goals_team_A > goals_team_B:
            return (A, B, goals_team_A, goals_team_B)
        elif goals_team_A < goals_team_B:
            return (B, A, goals_team_A, goals_team_B)
        else:
            return self._play_match(A, B)


    def make_championship(self):
        """Проводит все туры чемпионата"""

        for tour in range(self.tours):
            grouped_teams = self._group(self.teams, by=2)

            # Сыграть матчи между командами
            for A, B in grouped_teams:
                winner, loser, goals_A, goals_B = self._play_match(A, B)

                # Сохранить результат матча
                result_match = {
                    'winner': {'team': winner, 'goals': goals_A}, 
                    'loser': {'team': loser, 'goals': goals_B}
                }
                self.history[tour].append(result_match)

                # Исключить проигравшего из списка команд
                self.teams.remove(loser)




if __name__ == '__main__':
    teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    playoff = Playoff(teams)
    playoff.make_championship()

    print (teams)
    team = input('Choose your team: ')

    if team not in teams:
        print ('Your team is not on the team list :(')
        exit(0)

    # Показать историю матчей выбранной команды
    for tour, matchs in playoff.history.items():
        for match in matchs:
            winner, loser = match['winner'], match['loser']
            team_winner, team_loser = winner['team'], loser['team']
            goals_winner, goals_loser = winner['goals'], loser['goals']
                
            result = "Team '%s' won against Team '%s' in the '%d' round with a score of '%d:%d'"
            if team == team_winner or team == team_loser:
                print (result % (team_winner, team_loser, tour+1, goals_winner, goals_loser))
