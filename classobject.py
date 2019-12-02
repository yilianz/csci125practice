class bullet:
    def __init__(self,pos,speed):
        self.position = pos
        self.speed = speed

    def shoot(self):
        self.position += 10 * self.speed
        print(f"bullet is at postion {self.position}")

A = bullet(0, 6)
B = bullet(50, 2)
A.shoot()
B.shoot()