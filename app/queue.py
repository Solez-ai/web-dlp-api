"""
Queue system for managing download jobs using multiprocessing.
"""
import multiprocessing
from multiprocessing import Manager
from typing import Dict, Any
import uuid
import time

# Shared data structures across processes
manager = Manager()
job_queue = manager.Queue()
job_statuses = manager.dict()


def create_job(url: str, format: str) -> str:
    """
    Create a new download job.
    
    Args:
        url: YouTube video URL
        format: Output format (mp3 or mp4)
    
    Returns:
        job_id: Unique identifier for the job
    """
    job_id = str(uuid.uuid4())
    
    job_data = {
        'job_id': job_id,
        'url': url,
        'format': format,
        'status': 'queued',
        'progress': 0,
        'error': None,
        'filename': None,
        'created_at': time.time()
    }
    
    # Store job status
    job_statuses[job_id] = job_data
    
    # Add to queue
    job_queue.put(job_data)
    
    return job_id


def get_job_status(job_id: str) -> Dict[str, Any]:
    """
    Get the current status of a job.
    
    Args:
        job_id: Job identifier
    
    Returns:
        Job status dictionary or None if not found
    """
    return dict(job_statuses.get(job_id, {}))


def update_job_status(job_id: str, **kwargs):
    """
    Update job status with new information.
    
    Args:
        job_id: Job identifier
        **kwargs: Fields to update (status, progress, error, filename)
    """
    if job_id in job_statuses:
        job_data = dict(job_statuses[job_id])
        job_data.update(kwargs)
        job_statuses[job_id] = job_data


def delete_job(job_id: str):
    """
    Delete a job from the status tracking.
    
    Args:
        job_id: Job identifier
    """
    if job_id in job_statuses:
        del job_statuses[job_id]


def get_all_jobs() -> Dict[str, Dict[str, Any]]:
    """
    Get all jobs (used for cleanup).
    
    Returns:
        Dictionary of all jobs
    """
    return dict(job_statuses)
