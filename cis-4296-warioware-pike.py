import sys
import pygame
import asyncio

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
async def main():
	player = pygame.Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 100, 100)
	pygame.key.set_repeat(3)



	run = True
	while run:

		screen.fill((0, 0, 0))

		pygame.draw.rect(screen, (255, 0, 0), player)

		clock = pygame.time.Clock()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
					player.move_ip(-1, 0)
				if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
					player.move_ip(1, 0)
				if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
					player.move_ip(0, 1)
				if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
					player.move_ip(0, -1)

		clock.tick(60)

		pygame.display.update()

		await asyncio.sleep(0)

	pygame.quit()


asyncio.run(main())