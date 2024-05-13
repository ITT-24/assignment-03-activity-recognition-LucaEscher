# this skript will visualize the activity

import activity_recognizer as activity
import numpy as np
import os
import pyglet

IMG_SCALE = 0.2

# Load all Images
lifting_img_path = os.path.normpath('img/lifting_2.png')
lift_image = pyglet.image.load(lifting_img_path)

rowing_img_path = os.path.normpath('img/rowing_2.png')
row_image = pyglet.image.load(rowing_img_path)

running_img_path = os.path.normpath('img/running_2.png')
run_image = pyglet.image.load(running_img_path)

jumpingjacks_img_path = os.path.normpath('img/jumpingjack_2.png')
jump_image = pyglet.image.load(jumpingjacks_img_path)


class ActivityVisualizer:

    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.visualizer_state = 0
        self.classifier = activity.main()
        self.estimations = []
        
        # init sprites 
        self.lift_sprite = pyglet.sprite.Sprite(img=lift_image)
        self.row_sprite = pyglet.sprite.Sprite(img=row_image)
        self.run_sprite = pyglet.sprite.Sprite(img=run_image)
        self.jump_sprite = pyglet.sprite.Sprite(img=jump_image)
        self.current_sprite = None

        # adjust scale of sprites and position
        self.lift_sprite.scale = IMG_SCALE
        self.lift_sprite.x = self.window_width / 2 - self.lift_sprite.width / 2
        
        self.row_sprite.scale = IMG_SCALE
        self.row_sprite.x = self.window_width / 2 - self.row_sprite.width / 2
        
        self.run_sprite.scale = IMG_SCALE
        self.run_sprite.x = self.window_width / 2 - self.run_sprite.width / 2
        
        self.jump_sprite.scale = IMG_SCALE
        self.jump_sprite.x = self.window_width / 2 - self.jump_sprite.width / 2

    def update(self):
        match(self.visualizer_state):
            case 0:
                start_label = pyglet.text.Label(text='Press SPACE to WORKOUT!',
                                                font_name='ARIAL',
                                                font_size=20,
                                                bold=True,
                                                x=self.window_width//2, y=self.window_height//1.5,
                                                anchor_x='center', anchor_y='center',
                                                )
                start_label.color = (1, 1, 1, 255)
                start_label.draw()
                self.lift_sprite.draw()
            case 1:
                estimation = activity.real_time_estimation(self.classifier)
                print(estimation)
                
                self.estimations.append(estimation)
                
                if len(self.estimations) > 10:
                    if self.evaluate_estimations():
                        workout = None
                        pass
                    match(estimation):
                        case 0:
                            # jumpingjacks
                            jump_label = pyglet.text.Label(text='JUMPINGJACKS!',
                                                font_name='ARIAL',
                                                font_size=20,
                                                bold=True,
                                                x=self.window_width//2, y=self.window_height//1.5,
                                                anchor_x='center', anchor_y='center',
                                                )
                            jump_label.color = (1, 1, 1, 255)
                            jump_label.draw()
                            self.jump_sprite.draw()
                        case 1:
                            # lifting
                            lift_label = pyglet.text.Label(text='LIFTING!',
                                                font_name='ARIAL',
                                                font_size=20,
                                                bold=True,
                                                x=self.window_width//2, y=self.window_height//1.5,
                                                anchor_x='center', anchor_y='center',
                                                )
                            lift_label.color = (1, 1, 1, 255)
                            lift_label.draw()
                            self.lift_sprite.draw()
                        case 2:
                            # rowing
                            row_label = pyglet.text.Label(text='ROWING!',
                                                font_name='ARIAL',
                                                font_size=20,
                                                bold=True,
                                                x=self.window_width//2, y=self.window_height//1.5,
                                                anchor_x='center', anchor_y='center',
                                                )
                            row_label.color = (1, 1, 1, 255)
                            row_label.draw()
                            self.row_sprite.draw()
                        case 3:
                            # running
                            run_label = pyglet.text.Label(text='RUNNING!',
                                                font_name='ARIAL',
                                                font_size=20,
                                                bold=True,
                                                x=self.window_width//2, y=self.window_height//1.5,
                                                anchor_x='center', anchor_y='center',
                                                )
                            run_label.color = (1, 1, 1, 255)
                            run_label.draw()
                            self.run_sprite.draw
                        case _:
                            pass

    def draw(self):
        pass

    def run(self):
        pyglet.app.run()
        
    def evaluate_estimations(self):
        pass