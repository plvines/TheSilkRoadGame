# Copyright (c) 2022 Paul Vines

import networkx as nx
import itertools as it
import random

edges = [
    ("Kiev", "Cherson"),
    ("Cherson", "extra1"),
    ("extra1", "Atil"),
    ("Atil", "extra2"),
    ("extra2", "Samarkand"),
    ("Cherson", "Constantinople"),
    ("Venice", "Constantinople"),
    ("Constantinople", "extra4"),
    ("extra4", "Baku"),
    ("Constantinople", "Alexandria"),
    ("Tripoli", "Alexandria"),
    ("Alexandria", "Palmyra"),
    ("Constantinople", "Palmyra"),
    ("Palmyra", "Baghdad"),
    ("Alexandria", "Medina"),
    ("Medina", "Palmyra"),
    ("Baghdad", "Rayy"),
    ("Baku", "Merv"),
    ("Baku", "Atil"),
    ("Rayy", "Merv"),
    ("Merv", "Samarkand"),
    ("Merv", "Balkh"),
    ("Balkh", "Delhi"),
    ("Delhi", "extra5"),
    ("Calicut", "Delhi"),
    ("extra5", "Khotan"),
    ("Samarkand", "Kashgar"),
    ("Kashgar", "Khotan"),
    ("Kashgar", "Turfan"),
    ("Turfan", "Dunhuang"),
    ("Khotan", "Dunhuang"),
    ("Dunhuang", "Xian"),
]

RESOURCES = {
    "silk": "Xian",
    "fur": "Kiev",
    "wine": "Venice",
    "glass": "Tripoli",
    "spices": "Calicut",
    "incense": "Medina",
}
POSTS_TO_RESOURCES = {v: k for k, v in RESOURCES.items()}

GATEWAYS = {"Tripoli": "Alexandria",
            "Venice": "Constantinople",
            "Kiev": "Cherson",
            "Medina": "Palmyra",
            "Calicut": "Delhi",
            "Xian": "Dunhuang",
}

GW_TO_SOURCE = {v: k for k, v in GATEWAYS.items()}

BOARD = nx.Graph(edges)

REAL_NODES = {n for n in BOARD.nodes if 'extra' not in n}

DM = dict(nx.all_pairs_shortest_path_length(BOARD))

IMPORTANT_DESTS = {
    "Baghdad",
    "Rayy",
    "Balkh",
    "Kashgar",
    "Merv",
    "Samarkand"
}

def get_dsts(src, length, board=BOARD):
    return {
        node
        for node in board.nodes()
        if distance(src, node, board) == length and "extra" not in node
    }


def distance(src, dst, board=BOARD):
    return len(list(nx.shortest_simple_paths(board, src, dst))[0])


def res_distances(
    dst, resources={"venice", "tripoli", "xian", "medina", "kiev", "delhi"}, board=BOARD
):
    return [(src, distance(src, dst, board)) for src in resources]
