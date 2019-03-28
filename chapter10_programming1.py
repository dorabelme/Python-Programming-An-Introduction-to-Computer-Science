#starting point is cball4.py

from projectile import Projectile

def getInputs():
	a = float(input("Enter the launch angle(in degrees): "))
	v = float(input("Enter the initial velocity ( in meters/sec): "))
	h = float(input("Enter the initial height (in meters): "))
	t = float(input("Enter the time interval between position calculations: "))
	return a, v, h, t


def main():
	angle, vel, h0, time = getInputs()
	cball = Projectile(angle, vel, h0)
	prev_y = h0
	while cball.getY() >= prev_y:
		prev_y = cball.getY()
		cball.update(time)
	print("\nMaximum Height: {0:0.1f} meters".format(prev_y))
	

main()
