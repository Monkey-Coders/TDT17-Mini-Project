run:
	rm -f YOLO.out && chmod u+x yolo.slurm && sbatch yolo.slurm

queue:
	squeue -u zuimran

stop:
	scancel $(id)

stopall:
	scancel -u zuimran