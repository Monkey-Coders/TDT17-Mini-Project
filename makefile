run:
	chmod u+x yolo.slurm && sbatch yolo.slurm

test:
	chmod u+x yolo_test.slurm && sbatch yolo_test.slurm

queue:
	squeue -u zuimran

stop:
	scancel $(id)

stopall:
	scancel -u zuimran