class Player:
  def play(self):
      print("The Player is Playing cricket.")

  
class Batsman(Player):
  def play(self):
      print("The batsman is batting.")


class Bowler(Player):
  def play(self):
      print("The Bowler is bowling.")


batsman = Batsman()
bowler = Bowler()


batsman.play()
bowler.play()