from config import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, SPEED, SCORE, SPEED_LIMIT
from project import Enemy, Player,speedManager





def testSpeedManager():
    assert speedManager(11) ==11

def test_config_defined():
   assert SCREEN_WIDTH > 0
   assert SCREEN_HEIGHT > 0
   assert FPS == 50
   assert SPEED == 10
   assert SCORE == 0
   assert SPEED_LIMIT == 20

def test_player_init():
    player = Player()
    assert player

def test_enemy_init():
    enemy = Enemy()
    assert enemy 

def main():
    test_config_defined()
    testSpeedManager()
    test_player_init()
    test_enemy_init()



if __name__ == "__main__":
    main()