#!/usr/bin/env python3
"""This module defines a function that count the number of logs"""
import pymongo
from pymongo import MongoClient


db = client.logs
collection = db.nginx

def get_nginx_log_stats():
    """count total number of logs"""
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PATCH", "DELETE",]
    print("Methods:")

    for method in methods:
        count = collection.count_documents({"methods": method})
        print(f"\t{method}: {count}")

    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if name == "__main__":
    get_nginx_log_stats()
