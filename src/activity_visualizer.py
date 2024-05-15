# this skript will visualize the activity

import activity_recognizer as activity
import os
import pyglet

# decides how many predictions are taken into account while measuring
PREDICTION_ARRAY_LEN = 20

IMG_SCALE = 0.2
LABEL_COLOR_BLACK = (1, 1, 1, 255)

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
        self.predictions = []
        self.current_workout = None

        # init sprites
        self.lift_sprite = pyglet.sprite.Sprite(img=lift_image)
        self.row_sprite = pyglet.sprite.Sprite(img=row_image)
        self.run_sprite = pyglet.sprite.Sprite(img=run_image)
        self.jump_sprite = pyglet.sprite.Sprite(img=jump_image)

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
                # Start screen
                start_label = pyglet.text.Label(text='Press SPACE to WORKOUT!',
                                                font_name='ARIAL',
                                                font_size=20,
                                                bold=True,
                                                x=self.window_width//2, y=self.window_height//1.5,
                                                anchor_x='center', anchor_y='center',
                                                )
                description_label = pyglet.text.Label(text='You can row, lift, run or do jumingjacks!',
                                                      font_name='ARIAL',
                                                      font_size=16,
                                                      bold=True,
                                                      x=self.window_width//2, y=self.window_height//2,
                                                      anchor_x='center', anchor_y='center',
                                                      )
                start_label.color = LABEL_COLOR_BLACK
                description_label.color = LABEL_COLOR_BLACK

                start_label.draw()
                description_label.draw()
                self.lift_sprite.draw()
            case 1:
                prediction = activity.real_time_prediction(self.classifier)
                try:
                    self.predictions.append(prediction[0])
                except:
                    print(f'No data incoming. Is your input device on?')

                if len(self.predictions) >= PREDICTION_ARRAY_LEN:
                    self.current_workout = self.evaluate_predictions(self.predictions)
                    self.predictions.clear()

                match(self.current_workout):
                    case 0:
                        # jumpingjacks
                        jump_label = pyglet.text.Label(text='JUMPINGJACKS!',
                                                       font_name='ARIAL',
                                                       font_size=20,
                                                       bold=True,
                                                       x=self.window_width//2, y=self.window_height//1.5,
                                                       anchor_x='center', anchor_y='center',
                                                       )
                        jump_label.color = LABEL_COLOR_BLACK
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
                        lift_label.color = LABEL_COLOR_BLACK
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
                        row_label.color = LABEL_COLOR_BLACK
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
                        run_label.color = LABEL_COLOR_BLACK
                        run_label.draw()
                        self.run_sprite.draw()
                    case None:
                        description_label = pyglet.text.Label(text='Start running, rowing, lifting or jumpingjacks!!',
                                                              font_name='ARIAL',
                                                              font_size=14,
                                                              bold=True,
                                                              x=self.window_width//2, y=self.window_height//1.5,
                                                              anchor_x='center', anchor_y='center',
                                                              )
                        progress_label = pyglet.text.Label(text='Progressing …',
                                                           font_name='ARIAL',
                                                           font_size=14,
                                                           bold=True,
                                                           x=self.window_width//2, y=self.window_height//2.5,
                                                           anchor_x='center', anchor_y='center',
                                                           )

                        description_label.color = LABEL_COLOR_BLACK
                        progress_label.color = LABEL_COLOR_BLACK

                        description_label.draw()
                        progress_label.draw()

    def run(self):
        pyglet.app.run()

    # generated with ChatGPT and adjusted by me (see chatGPT.md)
    # Get the most frequent number in an array
    def evaluate_predictions(self, predictions):
        if not predictions:
            return None

        frequencies = {}
        for number in predictions:
            if number in frequencies:
                frequencies[number] += 1
            else:
                frequencies[number] = 1

        most_frequent = max(frequencies, key=frequencies.get)

        print(f'\nLegende: 0 = jumpingjack | 1 = lifting | 2 = rowing | 3 = running')
        print(f'\tPrediction Count: {frequencies}')
        print(f'\tMost Frequent: {most_frequent}')

        return most_frequent
