import pygame
import sys
import random
from pygame import mixer

pygame.init()
mixer.init()
pygame.key.set_repeat()
width = 800
height = 600

font = pygame.font.SysFont("monospace", 35)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
display_surface = pygame.display.set_mode((width, height))
class GameHub():
	def __init__(self, score, lives):
		#self.state = 'main_game'
		self.score = score
		self.lives = lives
		self.games_list = []
		#self.age = age



	def intro (self):
		flag = False
		time = 0
		bpm = 120
		beats = 0
		title_screen = pygame.image.load(r'assets/title_screen.png')
		instructions = pygame.image.load(r'assets/title_screen_instructions.png')
		selector_scale = [int(500//5), int(500//5)]
		selector = pygame.transform.scale(pygame.image.load(r'assets/title_screen_selector.png'), selector_scale)
		index = 1
		current_screen = title_screen

		while True:
			display_surface.blit(current_screen, (0, 0))
			time += 1
			if current_screen == instructions:
				pass
			elif index == 1:
				display_surface.blit(selector, (0, 490))
			elif index == -1:
				display_surface.blit(selector, (350, 490))
			#ticking = GameHub(0, 0).timer(time, bpm)
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
						if current_screen == instructions:
							pass
						else:
							index *= -1
					if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
						if current_screen == instructions:
							pass
						else:
							index *= -1
					if (event.key == pygame.K_SPACE):
						if current_screen == instructions:
							current_screen = title_screen
						elif index == 1:
							flag = True
						elif index == -1:
							current_screen = instructions

			if time % 60 == 0:
				#print("1 second has passed!")
				pass

			if time % ((30 * 60)/bpm) == 0:
				#screen.fill("red")
				#print("beat!")
				beats += 1
				#print(time / ((30 * 60)/bpm), beats)
			else:
				pass
				#screen.fill("black")

			if flag == True:
				break
			clock.tick(30)

			pygame.display.update()
			#print("This is the intro!")

	def display_lives(self, lives, bpm, state, max_beats):
		lives_scale = [int(400//2), int(300//2)]
		time = 0
		bg = pygame.image.load(r'assets/karate_background.jpg')
		gap = lives_scale[0]
		y_position = 0 + lives_scale[1]//2
		beats_list = []
		if state == "neutral":
			if max_beats == 8:
				GameHub(self.score, self.lives).play_music(bpm, "assets/warioware_start.wav")
			if max_beats == 4:
				GameHub(self.score, self.lives).play_music(bpm, "assets/warioware_neutral_alone.wav")
		if state == "happy":
			if max_beats == 8:
				GameHub(self.score, self.lives).play_music(bpm, "assets/warioware_celebrate.wav")
			if max_beats == 4:
				GameHub(self.score, self.lives).play_music(bpm, "assets/warioware_celebrate_alone.wav")
		if state == "sad":
			if max_beats == 8:
				GameHub(self.score, self.lives).play_music(bpm, "assets/warioware_failure.wav")
			if max_beats == 4:
				GameHub(self.score, self.lives).play_music(bpm, "assets/warioware_failure_alone.wav")

		while True:
			x_position = 0
			display_surface.blit(bg, [0, 0])
			time += 1
			beats = time / ((30 * 60)/bpm)
			lives_neutral = pygame.transform.scale(pygame.image.load(r'assets/hub_lives_neutral.png'), lives_scale)
			lives_happy = pygame.transform.scale(pygame.image.load(r'assets/hub_lives_happy.png'), lives_scale)
			lives_sad = pygame.transform.scale(pygame.image.load(r'assets/hub_lives_sad.png'), lives_scale)

			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					pygame.quit()
					sys.exit()
			if state == "neutral":
				reaction = lives_neutral
			elif state == "happy":
				reaction = lives_happy
			else:
				reaction = lives_sad
			if state == "sad":
				for life in range(lives + 1):
					display_surface.blit(reaction, [x_position, y_position])
					x_position += gap
			else:
				for life in range(lives):
					display_surface.blit(reaction, [x_position, y_position])
					x_position += gap
			if (max_beats == 4 and state == "neutral"):
				GameHub(self.score, self.lives).display_score(self.score)
			elif beats <= 4 or (max_beats == 4 and state != "neutral"):
				GameHub(self.score, self.lives).display_score(self.score - 1)
			else:
				GameHub(self.score, self.lives).display_score(self.score)
			clock.tick(30)
			pygame.display.update()
			#if beats - int(beats) < 0.05:
			#	beats = int(beats)
			#print(beats)
			#if beats % 1 == 0:
			#	print(int(beats))
			#	y_position = 0 + lives_scale[1]//3
			#else:
			if beats < 1:
				y_position = y_position / 3 / (beats + 1)
			else:
				y_position = y_position / 3 / beats
			#print(y_position)
			beats_list.append(beats)
			if len(beats_list) > 2:
				if beats_list[-1] >= int(beats) and beats_list[-2] <= int(beats):
				#if beats % 1 == 0:
					#print(int(beats))
					y_position = 0 + lives_scale[1]//3
			else:
				if beats < 1:
					y_position = y_position / 3 / (beats + 1)
				else:
					y_position = y_position / 3 / beats
					#print(y_position)
					
			if beats >= 4:
				state = "neutral"
			if beats >= max_beats:
				return beats
	def play_music(self, bpm, name):
		if bpm <= 100:
			pygame.mixer.music.load(name)
			pygame.mixer.music.play()
		else:
			name_components = name.split(".")
			name = name_components[0] + "_" + str(bpm) + "." + name_components[1]
			pygame.mixer.music.load(name)
			pygame.mixer.music.play()
			#time.sleep(2)
			#pygame.mixer.music.stop()
	def display_change_up(self, lives, bpm, state, change):
		lives_scale = [int(400//2), int(300//2)]
		time = 0
		bg = pygame.image.load(r'assets/karate_background.jpg')
		speed_up = pygame.transform.scale(pygame.image.load(r'assets/hub_speed_up.png'), (800, 222))
		level_up = pygame.transform.scale(pygame.image.load(r'assets/hub_level_up.png'), (800, 222))
		gap = lives_scale[0]
		y_position = 0 + lives_scale[1]//2
		beats_list = []
		GameHub(self.score, self.lives).play_music(bpm, "assets/warioware_changeup.wav")
		while True:
			x_position = 0
			display_surface.blit(bg, [0, 0])
			time += 1
			beats = time / ((30 * 60)/bpm)
			lives_neutral = pygame.transform.scale(pygame.image.load(r'assets/hub_lives_neutral.png'), lives_scale)
			lives_happy = pygame.transform.scale(pygame.image.load(r'assets/hub_lives_happy.png'), lives_scale)
			lives_sad = pygame.transform.scale(pygame.image.load(r'assets/hub_lives_sad.png'), lives_scale)

			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					pygame.quit()
					sys.exit()
			if state == "neutral":
				reaction = lives_neutral
			elif state == "happy":
				reaction = lives_happy
			else:
				reaction = lives_sad
			for life in range(lives):
				display_surface.blit(reaction, [x_position, y_position])
				x_position += gap
			GameHub(self.score, self.lives).display_score(self.score - 1)
			clock.tick(30)
			if change == "speed":
				display_surface.blit(speed_up, [0, 150])
			if change == "level":
				display_surface.blit(level_up, [0, 150])

			pygame.display.update()
			#if beats - int(beats) < 0.05:
			#	beats = int(beats)
			#print(beats)
			#if beats % 1 == 0:
			#	print(int(beats))
			#	y_position = 0 + lives_scale[1]//3
			#else:
			if beats < 1:
				y_position = y_position / 3 / (beats + 1)
			else:
				y_position = y_position / 3 / beats
			#print(y_position)
			beats_list.append(beats)
			if len(beats_list) > 2:
				if beats_list[-1] >= int(beats) and beats_list[-2] <= int(beats):
				#if beats % 1 == 0:
					#print(int(beats))
					y_position = 0 + lives_scale[1]//3
			else:
				if beats < 1:
					y_position = y_position / 3 / (beats + 1)
				else:
					y_position = y_position / 3 / beats
					#print(y_position)
					
			if beats >= 4:
				state = "neutral"
			if beats >= 8:
				return beats
	def display_score(self, score):
		score_scale = [int(200//1.1), int(300//1.1)]
		score_0 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_0.png'), score_scale)
		score_1 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_1.png'), score_scale)
		score_2 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_2.png'), score_scale)
		score_3 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_3.png'), score_scale)
		score_4 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_4.png'), score_scale)
		score_5 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_5.png'), score_scale)
		score_6 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_6.png'), score_scale)
		score_7 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_7.png'), score_scale)
		score_8 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_8.png'), score_scale)
		score_9 = pygame.transform.scale(pygame.image.load(r'assets/hub_score_9.png'), score_scale)
		ones = score % 10
		tens = int(score / 10)
		#print(ones, tens)
		if ones == 0:
			ones_image = score_0
		elif ones == 1:
			ones_image = score_1
		elif ones == 2:
			ones_image = score_2
		elif ones == 3:
			ones_image = score_3
		elif ones == 4:
			ones_image = score_4
		elif ones == 5:
			ones_image = score_5
		elif ones == 6:
			ones_image = score_6
		elif ones == 7:
			ones_image = score_7
		elif ones == 8:
			ones_image = score_8
		else:
			ones_image = score_9
		if tens == 0:
			tens_image = score_0
		elif tens == 1:
			tens_image = score_1
		elif tens == 2:
			tens_image = score_2
		elif tens == 3:
			tens_image = score_3
		elif tens == 4:
			tens_image = score_4
		elif tens == 5:
			tens_image = score_5
		elif tens == 6:
			tens_image = score_6
		elif tens == 7:
			tens_image = score_7
		elif tens == 8:
			tens_image = score_8
		else:
			tens_image = score_9
		display_surface.blit(ones_image, [width//2, height//2])
		display_surface.blit(tens_image, [width//2 - score_scale[0],height//2])
	def game_over (self, score):
		flag = False
		time = 0
		bpm = 120
		beats = 0
		bg = pygame.image.load(r'assets/karate_background.jpg')
		game_over = pygame.transform.scale(pygame.image.load(r'assets/hub_game_over.png'), (800, 222))

		while True:
			display_surface.blit(bg, (0, 0))
			time += 1
			#ticking = GameHub(0, 0).timer(time, bpm)
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						#print("You pressed space!")
						flag = True
			#if time % 60 == 0:
				#print("1 second has passed!")
			#	pass

			#if time % ((30 * 60)/bpm) == 0:
				#screen.fill("red")
				#print("beat!")
			#	beats += 1
				#print(time / ((30 * 60)/bpm), beats)
			#else:
				pass
				#screen.fill("black")

			#if flag == True:
			#	break
			if flag == True:
				break
			display_surface.blit(game_over, [0, 150])
			GameHub(score, 0).display_score(score)

			clock.tick(30)

			pygame.display.update()
			#print("This is the intro!")

	def choose_game(self, bpm, games_list, level):
		number_of_microgames = 5
		roll = random.randint(1, number_of_microgames)
		if len(games_list) == number_of_microgames - 1:
			games_list.pop(0)
		if len(games_list) > 0 and (roll in games_list):
			while roll in games_list:
				roll = random.randint(1, number_of_microgames)
		games_list.append(roll)
		#roll = 2
		if roll == 1:
			result = Transform_Microgame().game(bpm, level)
		if roll == 2:
			result = Hammer_Microgame().game(bpm, level)
		if roll == 3:
			result = Rain_Dodger().game(bpm, level)
		if roll == 4:
			result = Karate().game(bpm, level)
		if roll == 5:
			result = Rps().game(bpm, level)
		return result
	def timer(self, time, bpm):
		bomb_8 = pygame.image.load(r'assets/hub_bomb_8.png')
		bomb_7 = pygame.image.load(r'assets/hub_bomb_7.png')
		bomb_6 = pygame.image.load(r'assets/hub_bomb_6.png')
		bomb_5 = pygame.image.load(r'assets/hub_bomb_5.png')
		bomb_4 = pygame.image.load(r'assets/hub_bomb_4.png')
		bomb_3 = pygame.image.load(r'assets/hub_bomb_3.png')
		bomb_2 = pygame.image.load(r'assets/hub_bomb_2.png')
		bomb_1 = pygame.image.load(r'assets/hub_bomb_1.png')
		bomb_0 = pygame.image.load(r'assets/hub_bomb_0.png')
		beats = time / ((30 * 60)/bpm) 
		#print(beats)
		if beats <= 1:
			timer = bomb_7
		elif beats <= 2:
			timer = bomb_6
		elif beats <= 3:
			timer = bomb_5
		elif beats <= 4:
			timer = bomb_4
		elif beats <= 5:
			timer = bomb_3
		elif beats <= 6:
			timer = bomb_2
		elif beats <= 7:
			timer = bomb_1
		else:
			timer = bomb_0

		display_surface.blit(timer, (0, height - 152))
		return beats
		
class Rps():
	def game(self, bpm, level):
		import pygame
		import sys
		import random

		pygame.init()
		pygame.key.set_repeat()
		width = 800
		height = 600

		font = pygame.font.SysFont("monospace", 35)
		clock = pygame.time.Clock()

		screen = pygame.display.set_mode((width, height))
		display_surface = pygame.display.set_mode((width, height))

		rps_scale = [int(400//1.2), int(324//1.2)]
		space_scale = [int(1000//16), int(500//16)]
		keys_scale = [int(500//16), int(500//16)]
		command_scale = [int(800//3), int(398//3)]
		game_over = False
		time = 0
		background = pygame.image.load(r'assets/rps_background.png')
		player_neutral = pygame.transform.scale(pygame.image.load(r'assets/rps_neutral.png'), rps_scale)
		player_rock = pygame.transform.scale(pygame.image.load(r'assets/rps_rock.png'), rps_scale)
		player_paper = pygame.transform.scale(pygame.image.load(r'assets/rps_paper.png'), rps_scale)
		player_scissors = pygame.transform.scale(pygame.image.load(r'assets/rps_scissors.png'), rps_scale)

		enemy_neutral = pygame.transform.scale(pygame.image.load(r'assets/rps_enemy_neutral.png'), rps_scale)
		enemy_rock = pygame.transform.scale(pygame.image.load(r'assets/rps_enemy_rock.png'), rps_scale)
		enemy_paper = pygame.transform.scale(pygame.image.load(r'assets/rps_enemy_paper.png'), rps_scale)
		enemy_scissors = pygame.transform.scale(pygame.image.load(r'assets/rps_enemy_scissors.png'), rps_scale)

		space = pygame.transform.scale(pygame.image.load(r'assets/transform_space.png'), space_scale)
		left = pygame.transform.scale(pygame.image.load(r'assets/transform_left.png'), keys_scale)
		right = pygame.transform.scale(pygame.image.load(r'assets/transform_right.png'), keys_scale)

		win = pygame.transform.scale(pygame.image.load(r'assets/rps_win.png'), command_scale)
		lose = pygame.transform.scale(pygame.image.load(r'assets/rps_lose.png'), command_scale)


		display_surface.blit(background, (0, 0))

		enemy_switches = []
		command_list = []
		menu_index = 1
		player_index = 0
		def simple_enemy():
			if len(enemy_switches) < 1:
				choice = random.randint(1, 3)
				enemy_switches.append(choice)
			if enemy_switches[0] == 1:
				image = enemy_rock
			elif enemy_switches[0] == 2:
				image = enemy_paper
			else:
				image = enemy_scissors
			display_surface.blit(image, (width - rps_scale[0], int(height//2.5) ))

		def intermediate_enemy():
			if len(enemy_switches) < 1:
				choice = random.randint(1, 3)
				enemy_switches.append(choice)
			elif len(enemy_switches) < 2:
				roll = random.random()
				if roll < 0.04:
					choice = random.randint(1,3)
					if choice != enemy_switches[-1]:
						enemy_switches.append(choice)
				#print(roll, enemy_switches)
			if enemy_switches[-1] == 1:
				image = enemy_rock
			elif enemy_switches[-1] == 2:
				image = enemy_paper
			else:
				image = enemy_scissors
			display_surface.blit(image, (width - rps_scale[0], int(height//2.5) ))

		def expert_enemy(bpm):
			if len(enemy_switches) < 1:
				choice = random.randint(1, 3)
				enemy_switches.append(choice)
			elif len(enemy_switches) < 3:
				roll = random.random()
				if bpm > 160:
					roll_2 = random.random()
				else:
					roll_2 = 1
				if roll < 0.04 or roll_2 < 0.04:
					choice = random.randint(1,3)
					if choice != enemy_switches[-1]:
						enemy_switches.append(choice)
				#print(roll, enemy_switches)
			if enemy_switches[-1] == 1:
				image = enemy_rock
			elif enemy_switches[-1] == 2:
				image = enemy_paper
			else:
				image = enemy_scissors
			display_surface.blit(image, (width - rps_scale[0], int(height//2.5) ))

		def still_enemy(time):
			if enemy_switches[-1] == 1:
				image = enemy_rock
			elif enemy_switches[-1] == 2:
				image = enemy_paper
			else: 
				image = enemy_scissors
			#if time > 30:
				#image = enemy_neutral
			display_surface.blit(image, (width - rps_scale[0], int(height//2.5) ))

		def menu_display(index):
			button_horiz_size = 120
			button_vert_size = 90
			gap = 10 + button_horiz_size
			menu_scale = [int(rps_scale[0] // 3), int(rps_scale[1]//3)]
			xlocation = int(0 + width//8)
			ylocation = int(height//50)
			selector_size = 10
			if index == 1:
				selector_xlocation = xlocation - selector_size
			elif index == 2:
				selector_xlocation = xlocation + gap - selector_size
			else:
				selector_xlocation = xlocation + gap + gap - selector_size
			selector_ylocation = ylocation - selector_size
			pygame.draw.rect(screen, "red", (selector_xlocation, selector_ylocation, button_horiz_size + 2 *selector_size, 
				button_vert_size + 2 * selector_size) )
			pygame.draw.rect(screen, "white", (xlocation, ylocation, button_horiz_size, button_vert_size))
			pygame.draw.rect(screen, "white", (xlocation + gap, ylocation, button_horiz_size, button_vert_size))
			pygame.draw.rect(screen, "white", (xlocation + gap + gap, ylocation, button_horiz_size, button_vert_size))
			menu_rock = pygame.transform.scale(player_rock, menu_scale)
			menu_paper = pygame.transform.scale(player_paper, menu_scale)
			menu_scissors = pygame.transform.scale(player_scissors, menu_scale)
			display_surface.blit(menu_rock, (xlocation, ylocation))
			display_surface.blit(menu_paper, (xlocation + gap, ylocation))
			display_surface.blit(menu_scissors, (xlocation + gap + gap, ylocation))
			display_surface.blit(space, (selector_xlocation + button_horiz_size + 2 * selector_size - space_scale[0],
			 selector_ylocation + button_vert_size + 2 * selector_size - space_scale[1]))
			display_surface.blit(left, (selector_xlocation, selector_ylocation + button_vert_size + 2 * selector_size - space_scale[1]))
			display_surface.blit(right, (selector_xlocation + keys_scale[0], selector_ylocation + button_vert_size + 2 * selector_size - space_scale[1]))


		def player_choice(player_index):
			if player_index == 0:
				display_surface.blit(player_neutral, (0, int(height//2.5) ))
			elif player_index == 1:
				display_surface.blit(player_rock, (0, int(height//2.5) ))
			elif player_index == 2:
				display_surface.blit(player_paper, (0, int(height//2.5) ))
			else:
				display_surface.blit(player_scissors, (0, int(height//2.5) ))

		def winner_check(player_index, enemy_index):
			if player_index == 1 and enemy_index == 3:
				return True
			elif player_index == 2 and enemy_index == 1:
				return True
			elif player_index == 3 and enemy_index == 2:
				return True
			else:
				return False

		def win_or_lose(time, level):
			if len(command_list) == 0:
				if level == 1:
					command = win
				elif level == 2:
					command = lose
				else:
					roll = random.randint(1,2)
					if roll == 1:
						command = win
					if roll == 2:
						command = lose
				command_list.append(command)
			command = command_list[0]
			if time < 30:
				display_surface.blit(command, [int(width//2 - command_scale[0]//2), int(height//1.4)])

		def loser_check(player_index, enemy_index):
			if player_index == 1 and enemy_index == 2:
				return True
			elif player_index == 2 and enemy_index == 3:
				return True
			elif player_index == 3 and enemy_index == 1:
				return True
			else:
				return False

		def enemy_difficulty_selector(level):
			if level == 1:
				simple_enemy()
			elif level == 2:
				#intermediate_enemy()
				simple_enemy()
			else:
				expert_enemy(bpm)


		timer = 5
		success = False
		GameHub(2, 2).play_music(bpm, "assets/rps.wav")
		while game_over == False:
			#print(menu_index)
			player_choice(player_index)
			enemy_difficulty_selector(level)
			menu_display(menu_index)

			#display_surface.blit(enemy_neutral, (width - rps_scale[0], int(height//2.5) ))
			time += 1
			win_or_lose(time, level)
			ticking = GameHub(5, 5).timer(time, bpm)
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
						if menu_index == 1:
							menu_index = 3
						else:
							menu_index -=1
					if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
						if menu_index == 3:
							menu_index = 1
						else:
							menu_index +=1
					if (event.key == pygame.K_SPACE):
						player_index = menu_index
						if command_list[0] == win:
							decision = winner_check(player_index, enemy_switches[-1])
						elif command_list[0] == lose:
							decision = loser_check(player_index, enemy_switches[-1])
						if decision:
							#print("You Win!")
							success = True
						else:
							#print("You Lose!")
							success = False
						game_over = True
			if ticking >= 8:
				return success
			#if timer == 0:
				#game_over = True
			#timer_text = "Time:" + str(timer)
			#timer_label = font.render(timer_text, 1, "red")
			#screen.blit(timer_label, (0, height - (height / 15)))
			pygame.display.update()
			display_surface.blit(background, (0,0))
			clock.tick(30)
		while game_over == True:
			time += 1
			player_choice(player_index)
			still_enemy(time)
			menu_display(menu_index)
			if success:
				pygame.draw.line(screen, "green", (int(width//2), int(height//2) + int(height//2.3)), (int(width//1.5), int(height//9) + int(height//2.3)),  50)
				pygame.draw.line(screen, "green", (int(width//3), int(height//2) + int(height//4.9)), (int(width//2), int(height//2) + int(height//2.3)),  50)
			else:
				pygame.draw.line(screen, "red", (int(width//3), int(height//2) + int(height//2.3)), (int(width//1.5), int(height//9) + int(height//2.3)),  50)
				pygame.draw.line(screen, "red", (int(width//3), int(height//9) + int(height//2.3)), (int(width//1.5), int(height//2) + int(height//2.3)),  50)
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					sys.exit()
			ticking = GameHub(5, 5).timer(time, bpm)
			if ticking >= 8:
				return success
			pygame.display.update()
			display_surface.blit(background, (0,0))
			clock.tick(30)

class Karate():
	def game(self, bpm, level):
		import pygame
		import sys
		import random
		import math

		pygame.init()
		width = 800
		height = 600

		font = pygame.font.SysFont("monospace", 35)
		clock = pygame.time.Clock()

		screen = pygame.display.set_mode((width, height))
		display_surface = pygame.display.set_mode((width, height))

		game_over = False
		time = 0
		post_time = 0
		score = 0

		karate_girl = pygame.image.load(r"assets/karate_neutral.png")
		karate_girl_success = pygame.image.load(r'assets/karate_success.png')
		karate_girl_failure = pygame.image.load(r'assets/karate_fail.png')
		boulder = pygame.image.load(r'assets/karate_boulder.png')
		soda_can = pygame.image.load(r'assets/karate_soda_can.png')
		ufo = pygame.image.load(r'assets/karate_ufo.png')
		broken = pygame.image.load(r'assets/karate_broken.png')

		karate_girl_scale = (int(900 // 1.8), int(923 // 1.8))
		object_scale = (800//8, 800//8)

		boulder = pygame.transform.scale(boulder, object_scale)
		soda_can = pygame.transform.scale(soda_can, object_scale)
		ufo = pygame.transform.scale(ufo, object_scale)
		broken = pygame.transform.scale(broken, object_scale)

		background = pygame.image.load(r'assets/karate_background.jpg')

		display_surface.blit(background, (0, 0))
		object_xlocation = -100
		object_ylocation = 0

		frame_buffer = 30
		expected_frame_buffer = frame_buffer
		flag = False

		command_scale = [int(1900//3), int(800//3)]
		command = pygame.transform.scale(pygame.image.load(r'assets/command_kick.png'), command_scale)



		def summon_object(boulder, soda_can, ufo):
			roll = random.random()
			return True
			#if roll < .10:
			#	return True
			#else:
			#	return False

		def units_randomizer():
			units = random.randint(6, 8) * (bpm/120)
			return units

		def detect_collision(object_xlocation, object_ylocation):
			xhitbox = list(range(object_xlocation, object_xlocation + 101))
			yhitbox = list(range(object_ylocation, object_ylocation + 101))
			first_flag = False
			second_flag = False
			for coordinate in xhitbox:
				if coordinate >= width//2.1 and coordinate <= width//2.1 + width//5.5:
					first_flag = True
					#print("first_flag True")
					break
			for coordinate in yhitbox:
				if coordinate >= height//2.5 and coordinate <= height//2.5 + height // 6:
					second_flag = True
					#print("second_flag True")
					break
			if first_flag and second_flag:
				return True
			else:
				return False

		def object_decider(level):
			if level == 1:
				return "boulder"
			elif level == 2:
				return "soda_can"
			else:
				return "ufo"


		def move_boulder(object_xlocation, object_ylocation, units):
			object_xlocation += units
			object_ylocation = int(height//2.5)
			return[object_xlocation, object_ylocation]

		def move_soda_can(object_xlocation, object_ylocation, units):
			object_xlocation += units
			object_ylocation = int((0.005 * (object_xlocation ** 2)) - (2.6 * object_xlocation)) + 500
			return [object_xlocation, object_ylocation]


		def move_ufo(object_xlocation, object_ylocation, units):
			object_xlocation += units	
			object_ylocation = int(100 * math.sin(0.025 * object_xlocation) + 300)
			return [object_xlocation, object_ylocation]


		GameHub(2, 2).play_music(bpm, "assets/karate.wav")
		while game_over == False:
			time+=1
			ticking = GameHub(5, 5).timer(time, bpm)
			if (frame_buffer != expected_frame_buffer):
				frame_buffer += 1
				state = pygame.transform.scale(pose, karate_girl_scale)
			else:
				state = pygame.transform.scale(karate_girl, karate_girl_scale)
			display_surface.blit(state, (width//2.5, 90))
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						test = detect_collision(object_xlocation, object_ylocation)
						if test:
							pose = karate_girl_success
							flag = False
							success = True
							game_over = True
							break
						else:
							pose = karate_girl_failure
							success = False
							game_over = True
							break
						#pygame.draw.rect(screen, "red", (width//2.1, height//2.5, width//5.5, height//6))
						frame_buffer = 0
			if flag == False:
				flag = summon_object(boulder, soda_can, ufo)
				units = units_randomizer()
				projectile = object_decider(level)
			if flag == True:
				if projectile == "boulder":
					object_coordinates = move_boulder(object_xlocation, object_ylocation, units)
					#object_xlocation += units
					#object_ylocation = int(height//2.5)
					object_xlocation = int(object_coordinates[0])
					object_ylocation = int(object_coordinates[1])
					display_surface.blit(boulder, (object_xlocation, object_ylocation))
				elif projectile == "soda_can":
					object_coordinates = move_soda_can(object_xlocation, object_ylocation, units)
					#object_xlocation += units
					#object_ylocation = int(height//2.5)
					object_xlocation = int(object_coordinates[0])
					object_ylocation = int(object_coordinates[1])
					#print(object_xlocation, object_ylocation)
					display_surface.blit(soda_can, (object_xlocation, object_ylocation))
				#print("It works!")
				else:
					object_coordinates = move_ufo(object_xlocation, object_ylocation, units)
					#object_xlocation += units
					#object_ylocation = int(height//2.5)
					object_xlocation = int(object_coordinates[0])
					object_ylocation = int(object_coordinates[1])
					#print(object_xlocation, object_ylocation)
					display_surface.blit(ufo, (object_xlocation, object_ylocation))
			if object_xlocation + 101 > width//2.1 + width//5.5:
				success = False
				game_over = True
				pose = karate_girl
			if ticking <= 2:
				display_surface.blit(command, [(width - command_scale[0])//2, (height - command_scale[1])//2])
			pygame.display.update()
			display_surface.blit(background, (0, 0))
			clock.tick(30)

		while game_over == True:
			time += 1
			ticking = GameHub(5, 5).timer(time, bpm)
			state = pygame.transform.scale(pose, karate_girl_scale)
			display_surface.blit(state, (width//2.5, 90))
			if post_time < 15 and success:
				display_surface.blit(broken, (object_xlocation, object_ylocation))
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					sys.exit()
			if success:
				end_text = "You Win!"
			else:
				object_ylocation += 10
				if projectile == "boulder":
					display_surface.blit(boulder, (object_xlocation, object_ylocation))
				if projectile == "soda_can":
					display_surface.blit(soda_can, (object_xlocation, object_ylocation))
				if projectile == "ufo":
					display_surface.blit(ufo, (object_xlocation, object_ylocation))
				end_text = "You Lose!"
			#end_label = font.render(end_text, 10, "green")
			#screen.blit(end_label, (0, height - height//6))
			pygame.display.update()
			display_surface.blit(background, (0, 0))
			if ticking >= 8:
				return success
			clock.tick(30)
class Rain_Dodger():
	def game(self, bpm, level):
		import pygame
		import sys
		import random
		pygame.init()
		pygame.key.set_repeat(3)
		width = 800
		height = 600

		screen = pygame.display.set_mode((width, height))
		time = 0
		game_over = False
		player_size = 50
		player_pos = [width/2, height - 2 * player_size]

		enemy_size = player_size
		enemy_pos = [random.randint(0, width - enemy_size), 0]
		enemy_list = [enemy_pos]

		speed = 10 * (bpm/120)

		clock = pygame.time.Clock()
		font = pygame.font.SysFont("monospace", 35)
		score = 0
		score_milestones = []

		command_scale = [int(1900//3), int(800//3)]
		command = pygame.transform.scale(pygame.image.load(r'assets/command_dodge.png'), command_scale)
		def set_level(time, speed, score_milestones):
			if time % 300 == 0:
				speed += 3
			#print(speed)
			return speed
		def drop_enemies(enemy_list):
			delay = random.random()
			if level == 1:
				threshold = 10
				probability = 0.20
			elif level == 2:
				threshold = 18
				probability = 0.25
			else:
				threshold = 40
				probability = 0.40
			if len(enemy_list) < threshold and delay < probability:
				if level == 1:
					y_pos = -10
					x_pos = random.randint(0, width)
				elif level == 2:
					x_pos = -10
					y_pos = random.randint(0, height)
				else:
					x_pos = random.randint(- (width), width - player_size)
					y_pos = random.uniform(-1, 1)
				enemy_list.append([x_pos, y_pos])

		def draw_enemies(enemy_list):
			for enemy_pos in enemy_list:
				pygame.draw.rect(screen, "red", (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)) 

		def update_enemy_positions(enemy_list):
			for i, enemy_pos in enumerate(enemy_list):
					if (enemy_pos[1] >= -10 and enemy_pos[1] < height) and (enemy_pos[0] < width):
						if level == 1:
							enemy_pos[1] += speed
						elif level == 2:
							enemy_pos[0] += speed
						else:
							enemy_pos[1] += speed
							enemy_pos[0] += speed
					else:
						enemy_list.pop(i)


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

		success = True
		background = pygame.image.load(r'assets/rain_dodge_background.png')
		GameHub(2, 2).play_music(bpm, "assets/rain_dodge.wav")


		while game_over == False: 
			display_surface.blit(background, (0, 0))
			time += 1
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:

					x = player_pos[0]
					y = player_pos[1]
					unit = 2.5 * (bpm/120)
					if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
						if x > 0:
							x -= unit
					if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
						if x < width - player_size:
							x += unit
					if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
						if y > 0:
							y -= unit
					if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
						if y < height - player_size:
							y += unit
					player_pos = [x,y]
					#print(y)
					if (event.key == pygame.K_ESCAPE):
						sys.exit()
			#screen.fill("black")



			drop_enemies(enemy_list)
			update_enemy_positions(enemy_list)
			if time % 30 == 0:
				score += 1
			speed = set_level(time, speed, score_milestones)
			#text = "Score:" + str(score)
			#label = font.render(text, 1, "yellow")
			#screen.blit(label, (width - (width/4), height - (height / 15)))
			if collision_check(enemy_list, player_pos):
				game_over = True
				success = False
			draw_enemies(enemy_list)

			pygame.draw.rect(screen, "white", (player_pos[0], player_pos[1], player_size, player_size))
			pygame.draw.rect(screen, "red", (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)) 
			ticking = GameHub(5, 5).timer(time, bpm)
			if ticking <= 2:
				display_surface.blit(command, [(width - command_scale[0])//2, (height - command_scale[1])//2])
			if ticking >= 8:
				return success
			clock.tick(30)

			pygame.display.update()
		while game_over == True:
			display_surface.blit(background, (0, 0))
			time += 1
			ticking = GameHub(5, 5).timer(time, bpm)
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					sys.exit()
			#screen.fill("black")
			clock.tick(30)
			if ticking >= 8:
				return success

			pygame.display.update()

class Transform_Microgame():
	def __init__(self):
		#self.state = 'main_game'
		#self.name = name
		#self.age = age
		pass
	def game(self, bpm, level):
		import pygame
		import sys
		import random

		pygame.init()
		pygame.key.set_repeat()
		width = 800
		height = 600

		font = pygame.font.SysFont("monospace", 35)
		clock = pygame.time.Clock()

		screen = pygame.display.set_mode((width, height))
		display_surface = pygame.display.set_mode((width, height))
		command_scale = [int(1900//3), int(800//3)]

		game_over = False
		time = 0
		background = pygame.image.load(r'assets/transformation_background.png')

		direction_dict = {1:pygame.K_LEFT, 2:pygame.K_RIGHT, 3:pygame.K_UP, 4:pygame.K_DOWN, 5:pygame.K_SPACE}
		wasd_dict = {pygame.K_LEFT:pygame.K_a, pygame.K_RIGHT:pygame.K_d, pygame.K_UP:pygame.K_w, pygame.K_DOWN:pygame.K_s, pygame.K_SPACE:pygame.K_SPACE}

		up = pygame.image.load(r'assets/transform_up.png')
		down = pygame.image.load(r'assets/transform_down.png')
		left = pygame.image.load(r'assets/transform_left.png')
		right = pygame.image.load(r'assets/transform_right.png')
		space = pygame.image.load(r'assets/transform_space.png')

		pose = pygame.image.load(r'assets/transform_neutral_pose.png')
		pose_up = pygame.image.load(r'assets/transform_up_pose.png')
		pose_down = pygame.image.load(r'assets/transform_down_pose.png')
		pose_left = pygame.image.load(r'assets/transform_left_pose.png')
		pose_right = pygame.image.load(r'assets/transform_right_pose.png')
		pose_space = pygame.image.load(r'assets/transform_space_pose.png')

		failure = pygame.image.load(r'assets/transform_vegetable.png')
		success = pygame.image.load(r'assets/transform_success.png')
		poof = pygame.image.load(r'assets/transform_poof.png')

		scale = (500//5, 500//5)
		space_scale = (1000//5, 500//5)
		pose_scale = (int(800//2.5), int(800//2.5))

		command = pygame.transform.scale(pygame.image.load(r'assets/command_transform.png'), command_scale)

		up = pygame.transform.scale(up, scale)
		down = pygame.transform.scale(down, scale)
		left = pygame.transform.scale(left, scale)
		right = pygame.transform.scale(right, scale)
		space = pygame.transform.scale(space, space_scale)

		def get_directions(list_length):
			randomized_directions = []
			for i in range(list_length):
				direction = random.randint(1, 4)
				#print(direction_dict.get(direction))
				if i == list_length - 1:
					direction = 5
				randomized_directions.append(direction_dict.get(direction))
			return randomized_directions
		def wasd_conversion(direction_list):
			randomized_wasd = []
			for direction in direction_list:
				randomized_wasd.append(wasd_dict.get(direction))
			return randomized_wasd
		def image_display(direction_list):
			loops = 1
			gap = width/len(direction_list)
			for direction in direction_list:
				if direction == direction_dict[1]:
					display_surface.blit(left, (loops * gap - 50, 0))
				if direction == direction_dict[2]:
					display_surface.blit(right, (loops * gap - 50, 0))
				if direction == direction_dict[3]:
					display_surface.blit(up, (loops * gap - 50, 0))
				if direction == direction_dict[4]:
					display_surface.blit(down, (loops * gap - 50, 0))
				if direction == direction_dict[5]:
					display_surface.blit(space, (width//2 - width//8, 100))
				loops += 1

		if level == 1:
			correct_directions = get_directions(4)
		elif level == 2:
			correct_directions = get_directions(6)
		else:
			correct_directions = get_directions(9)
		correct_wasd = wasd_conversion(correct_directions)
		current_index = 0
		timer = 5
		#print(correct_wasd)
		succeed = False
		post_time = 0
		GameHub(2, 2).play_music(bpm, "assets/transform.wav")


		display_surface.blit(background, (0, 0))
		while game_over == False:
			time += 1
			ticking = GameHub(5, 5).timer(time, bpm)
			pose = pygame.transform.scale(pose, pose_scale)
			display_surface.blit(pose, (width//2 - width//5, height//2.5))
			if current_index == len(correct_directions) - 1:
				pygame.draw.rect(screen, "red", ((width // 2 - width // 8) - (width//2 - width//8)//16, 100, 1000//5 * 1.2, 500//5 * 1.2))
			else:
				pygame.draw.rect(screen, "red", ((current_index + 1) * width/len(correct_directions) - 60, 0, 500//5 * 1.2, 500//5 * 1.2))
			image_display(correct_directions)
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == correct_directions[current_index] or event.key == correct_wasd[current_index]:
						#print("It works!")
						current_index += 1
					else:
						#print("You lose!")
						pose = poof
						game_over = True
						break
					if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
						pose = pose_left
					if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
						pose = pose_right
					if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
						pose = pose_up
					if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
						pose = pose_down
					if (event.key == pygame.K_SPACE):
						pose = pose_space
			if current_index == len(correct_directions):
				#print("You win!")
				pose = poof
				game_over = True
				#time = 0
				succeed = True
			#if time % 30 == 0:
			#	timer -= 1
			#if timer == 0:
			#	game_over = True
			if ticking >= 8:
				return succeed
			#timer_text = "Time:" + str(timer)
			#timer_label = font.render(timer_text, 1, "red")
			#screen.blit(timer_label, (0, height - (height / 15)))
			if ticking <= 2:
				display_surface.blit(command, [(width - command_scale[0])//2, (height - command_scale[1])//2])
			pygame.display.update()
			display_surface.blit(background, (0,0))
			clock.tick(30)
		while game_over == True:
			time += 1
			post_time += int(1 * (bpm/100))
			ticking = GameHub(0, 0).timer(time, bpm)
			pose = pygame.transform.scale(pose, pose_scale)
			display_surface.blit(pose, (width//2 - width//5, height//2.5))
			display_surface.blit(pose, (width//2 - width//5, height//2.5))
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
					sys.exit()
			if current_index == len(correct_directions):
				end_text = "You Win!"
			else:
				end_text = "You Lose!"
			#end_label = font.render(end_text, 10, "yellow")
			#screen.blit(end_label, (0, height - height//6))
			if post_time % 20 == 0 and end_text == "You Win!":
				pose = success
			elif post_time % 20 == 0 and end_text == "You Lose!" and timer != 0:
				pose = failure
			if ticking >= 8:
				return succeed
				#break
			clock.tick(30)
			pygame.display.update()
			display_surface.blit(background, (0,0))

class Hammer_Microgame():
	def game(self, bpm, level):
		import pygame
		import sys

		pygame.init()
		pygame.key.set_repeat()
		width = 800
		height = 600

		font = pygame.font.SysFont("monospace", 35)
		clock = pygame.time.Clock()

		screen = pygame.display.set_mode((width, height))
		display_surface = pygame.display.set_mode((width, height))

		image = pygame.image.load(r'assets/hammer_windup.png')
		second_image = pygame.image.load(r'assets/hammer_hit.png')
		table = pygame.image.load(r'assets/hammer_table.png')
		nail = pygame.image.load(r'assets/hammer_nail.png')
		effect = pygame.image.load(r'assets/hammer_effect.png')

		image = pygame.transform.scale(image, (1080//2, 790//2))
		second_image = pygame.transform.scale(second_image, (1080//2, 790//2))
		table = pygame.transform.scale(table, (int(400//1.5), int(360//1.5)))
		nail = pygame.transform.scale(nail, (int(196 // 2.5), int(264 // 2.5)))
		effect = pygame.transform.scale(effect, (int(163//1.5), int(99//1.5)))
		background_image = pygame.image.load(r'assets/hammer_background.png')
		command_scale = [int(1900//3), int(800//3)]
		command = pygame.transform.scale(pygame.image.load(r'assets/command_hammer.png'), command_scale)

		current_display = image
		frame_buffer = 3
		initial_frame_buffer = 3

		if level == 1:
			required_hits = 8
		elif level == 2:
			required_hits = 12
		else:
			required_hits = 15
		#required_hits = 17
		timer = 8
		time_elapsed = 0
		total_required_hits = required_hits
		game_over = False
		succeed = False
		post_time = 0

		GameHub(2, 2).play_music(bpm, "assets/hammer.wav")
		while game_over == False:
			time_elapsed += 1
			display_surface.blit(background_image, (0, 0))
			display_surface.blit(nail, (0 + width // 8, (height/1.7) + (height/12) - required_hits/(total_required_hits/(height/12))))
			display_surface.blit(table, (0, height / 1.5))
			
			if frame_buffer != initial_frame_buffer:
				current_display = second_image
				frame_buffer += 1
				display_surface.blit(current_display, ((width/4) - (width//4.4), height/4))
				display_surface.blit(effect, ((width/4) - (width//4.4) + (163//1.5)/1.6, (height/1.7 - 99//1.5 + (600/50)) + (height/12) - required_hits/(total_required_hits/(height/12))))
			else:
				current_display = image
				display_surface.blit(current_display, ((width//1.6) - (width//4.4), height/4 + (height//30)))
			ticking = GameHub(5, 5).timer(time_elapsed, bpm)
			if ticking <= 2:
				display_surface.blit(command, [(width - command_scale[0])//2, (height - command_scale[1])//2])
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					#print("Key down!")
					if (event.key == pygame.K_ESCAPE):
						sys.exit()
					if (event.key == pygame.K_SPACE):
						#print("Space!")
						required_hits -= 1
						frame_buffer = 0

			#if time_elapsed % 30 == 0:
				#timer -= 1
			#timer_text = "Time:" + str(timer)
			#hits_text = "Hits Left:" + str(required_hits)
			#timer_label = font.render(timer_text, 1, "red")
			#hits_label = font.render(hits_text, 1, "red")
			#screen.blit(timer_label, (0, height - (height / 15)))
			#screen.blit(hits_label, (0, height - (height / 15) * 2))
			clock.tick(30)
			#if required_hits == 0 or timer == 0:
			if required_hits == 0 or ticking >= 8:
				game_over = True
			#print(ticking)

			pygame.display.update()
		while game_over == True:
			#print(ticking)
			time_elapsed += 1
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					sys.exit()
			display_surface.blit(background_image, (0, 0))
			display_surface.blit(nail, (0 + width // 8, (height/1.7) + (height/12) - required_hits/(total_required_hits/(height/12))))
			display_surface.blit(table, (0, height / 1.5))
			current_display = image
			display_surface.blit(current_display, ((width//1.6) - (width//4.4), height/4 + (height//30)))
			ticking = GameHub(5, 5).timer(time_elapsed, bpm)
			if required_hits == 0:
				end_text = "You Win!"
				succeed = True
			elif ticking >= 8:
				end_text = "You Lose!"
			else:
				end_text = "ERROR"
			end_label = font.render(end_text, 10, "white")
			screen.blit(end_label, (100, 100))
			if ticking >= 8:
				return succeed
			clock.tick(30)


			pygame.display.update()

while True:
	player = GameHub(1, 4)
	bpm = 100
	initial_bpm = bpm
	level = 1
	speed_up_intervals = 4
	level_up_intervals = 5
	state = "neutral"
	max_beats = 8
	GameHub(player.score, player.lives).intro()
	while True:
		pygame.key.set_repeat()
		beats = GameHub(player.score, player.lives).display_lives(player.lives, bpm, state, max_beats)
		if GameHub(player.score, player.lives).choose_game(bpm, player.games_list, level):
			state = "happy"
		else:
			state = "sad"
			player.lives -= 1
		player.score += 1
		#print(player.score, player.lives)
		if player.lives <= 0:
			break
		if player.score % speed_up_intervals == 0 and bpm <= initial_bpm * 2.20:
			GameHub(player.score, player.lives).display_lives(player.lives, bpm, state, 4)
			bpm *= 1.15
			bpm = int(bpm)
			#print("SPEED UP " + str(bpm))
			state = "neutral"
			GameHub(player.score, player.lives).display_change_up(player.lives, bpm, state, "speed")
			max_beats = 4
			continue
		elif player.score % level_up_intervals == 0 and level != 3:
			level += 1
			#print("LEVEL UP " + str(level))
			GameHub(player.score, player.lives).display_lives(player.lives, bpm, state, 4)
			state = "neutral"
			GameHub(player.score, player.lives).display_change_up(player.lives, bpm, state, "level")
			max_beats = 4
			continue
		else:
			max_beats = 8

	pygame.key.set_repeat(0)
	GameHub(player.score, player.lives).display_lives(0, bpm, "sad", 4)
	GameHub(player.score, player.lives).game_over(player.score - 1)

