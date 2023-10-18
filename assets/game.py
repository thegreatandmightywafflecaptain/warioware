# Code taken from https://www.youtube.com/watch?v=-8n91btt5d8&ab_channel=KeithGalli

import pygame
import sys
import random
pygame.init()
pygame.key.set_repeat(3)
width = 800
height = 600

screen = pygame.display.set_mode((width, height))

game_over = False
player_size = 50
player_pos = [width/2, height - 2 * player_size]

enemy_size = player_size
enemy_pos = [random.randint(0, width - enemy_size), 0]
enemy_list = [enemy_pos]

speed = 10

clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 35)
score = 0
score_milestones = []
def set_level(score, speed, score_milestones):
	if score < 20:
		speed = 5
		return speed
	if score % 20 == 0:
		if len(score_milestones) == 0 or score_milestones[-1] != score:
			score_milestones.append(score)
			speed += 3
	#print(speed)
	return speed
def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 17 and delay < 0.15:
		x_pos = random.randint(0, width - enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, "red", (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)) 

def update_enemy_positions(enemy_list, score):
	for i, enemy_pos in enumerate(enemy_list):
			if enemy_pos[1] >= 0 and enemy_pos[1] < height:
				enemy_pos[1] += speed
				#enemy_pos[0] += speed
			else:
				enemy_list.pop(i)
				score += 1
	return score

def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False


def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]
	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
			return True
	return False

while game_over == False: 
	for event in pygame.event.get():
		#print(clock)
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]
			unit = 2.5
			if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
				if x > 0:
					x -= unit
			if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
				if x < width - player_size:
					x += unit
			player_pos = [x,y]
	screen.fill("black")



	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	speed = set_level(score, speed, score_milestones)
	text = "Score:" + str(score)
	label = font.render(text, 1, "yellow")
	screen.blit(label, (width - (width/4), height - (height / 15)))
	if collision_check(enemy_list, player_pos):
		game_over = True
	draw_enemies(enemy_list)

	pygame.draw.rect(screen, "white", (player_pos[0], player_pos[1], player_size, player_size))
	pygame.draw.rect(screen, "red", (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)) 
	clock.tick(30)

	pygame.display.update()
