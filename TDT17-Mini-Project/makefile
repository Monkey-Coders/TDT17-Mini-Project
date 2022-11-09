run:
	rm -f slurm_output.out && chmod u+x job.slurm && sbatch job.slurm

queue:
	squeue -u zuimran

stop:
	scancel $(id)

stopall:
	scancel -u zuimran