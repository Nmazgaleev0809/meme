extends KinematicBody2D


# Called when the node enters the scene tree for the first time.
func _ready():

	velocity = Vector2(delta)
	
func _physics_process(delta):
