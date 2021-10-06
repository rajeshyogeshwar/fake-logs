"""Engine module to generate logs for Nginx.
Generated logs are in default Nginx format i.e. combined.

Sample:
xxx.xxx.xxx.xxx - - [dd/mmm/yyyy:hh:mm:ss +0000] "POST <path> HTTP/1.1" <response-code> <bytes> "<referrer>" "<user-agent>"
"""
import time
import numpy as np
import pandas as pd

from faker import Faker
from loguru import logger
from datetime import datetime
from ..webservers.paths import RequestedPath

class Nginx:
    """Nginx log generator."""

    @classmethod
    def generate_logs(cls, number_of_lines: int, interval: float, file_path: str):
        """Generate log lines and write them to file on the given path."""
        logger.info("Starting generation.")
        
        st = time.perf_counter()
        
        fk = Faker()
        ips = [fk.ipv4() for _ in range(500)]
        user_agents = [fk.user_agent() for _ in range(500)]
        paths = [RequestedPath.generate() for _ in range(500)]
        referrer = [fk.uri() for _ in range(500)]

        timestamps = pd.date_range(datetime.utcnow(), periods=(number_of_lines), freq=f"{interval}S").format(formatter=lambda dt: dt.strftime("%d/%b/%Y %H:%M:%S +0000"))
        
        df = pd.DataFrame()
        
        # Add IPs
        df["ip"] = np.random.choice(ips, size=number_of_lines)
        
        # Add timestamps
        df["timestamp"] = timestamps
        
        # Add requested paths
        df["path"] = np.random.choice(paths, size=number_of_lines)
        
        # Add response codes
        df["response_code"] = np.random.choice([200, 201, 400, 401, 403, 404, 500, 502, 504], size=number_of_lines)
        
        # Add bytes
        df["bytes"] = np.random.choice(np.random.random_integers(500, 2500), size=number_of_lines)
        
        # Add referrer
        df["referrer"] = np.random.choice(referrer, size=number_of_lines)
        
        # Add user agents
        df["user_agent"] = np.random.choice(user_agents, size=number_of_lines)

        # Concat all into the needed format
        df["log"] = df["ip"] + " - - [" + df["timestamp"] + "] \"" + df["path"] + "\" " + df["response_code"].astype(str) + " " + df["bytes"].astype(str) + "\"" + df["referrer"] + "\" \"" + df["user_agent"]

        # Use numpy to write the column to file at the specified path
        np.savetxt(file_path, df["log"].to_numpy(), fmt="%s")
        et = time.perf_counter()

        logger.info(f"{number_of_lines} logs generated in {round((et - st), 2)} seconds and saved to {file_path}.")
