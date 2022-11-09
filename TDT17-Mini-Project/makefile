run:
	rm -f FORMAT_DATA.out && chmod u+x job.slurm && sbatch job.slurm

queue:
	squeue -u zuimran

stop:
	scancel $(id)

stopall:
	scancel -u zuimran