extends KinematicBody2D
const UP = Vector2(0, -1)
const GRAVITY = 20
const ACCELERATION = 20
var MAX_SPEED = 150
const JUMP_HEIGHT = -300
var motion = Vector2()
func _physics_process(delta):
	motion.y += GRAVITY
	var friction = false
	if Input.is_action_pressed("ui_right"):
		motion.x = min(motion.x+ACCELERATION, MAX_SPEED)
		$Sprite.flip_h = false
		if MAX_SPEED == 200:
			$Sprite.play("run")
		else:
			$Sprite.play("walk")
	elif Input.is_action_pressed("ui_left"):
		motion.x = max(motion.x-ACCELERATION, -MAX_SPEED)
		$Sprite.flip_h = true
		if MAX_SPEED == 200:
			$Sprite.play("run")
		else:
			$Sprite.play("walk")
	else:
		$Sprite.play("idle")
		friction = true
	if is_on_floor():
		if Input.is_key_pressed(KEY_SHIFT):
			MAX_SPEED = 200
		else:
			MAX_SPEED = 100
		if Input.is_action_just_pressed("ui_up"):
			motion.y = JUMP_HEIGHT
		if friction == true:
			motion.x = lerp(motion.x, 0, 0.2)
	else:
		if motion.y < 0:
			$Sprite.play("jump")
		else:
			$Sprite.play("fall")
		if friction == true:
			motion.x = lerp(motion.x, 0, 0.05)
	motion = move_and_slide(motion, UP)
	pass