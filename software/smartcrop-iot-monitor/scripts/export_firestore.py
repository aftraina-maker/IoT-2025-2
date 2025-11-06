# -*- coding: utf-8 -*-
"""
Firestore export script for the SmartCrop IoT Monitor.
"""

import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

def export_firestore_to_csv(collection_name, output_file):
    """
    Exports a Firestore collection to a CSV file.
    """
    cred = credentials.Certificate("../api/firebase_key.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    docs = db.collection(collection_name).stream()
    data = []
    for doc in docs:
        data.append(doc.to_dict())

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Successfully exported collection '{collection_name}' to '{output_file}'")

if __name__ == "__main__":
    # Example usage:
    # export_firestore_to_csv("sensor_data", "sensor_data.csv")
    print("Usage: Call export_firestore_to_csv(collection_name, output_file) with your desired collection and output file.")
