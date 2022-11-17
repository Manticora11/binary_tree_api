from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from binary_tree import *


app = FastAPI()


class CreateTreeData(BaseModel):
    nodes: List[List[int]]


class FindAncestorData(BaseModel):
    nodes: List[List[int]]
    first_number: int
    second_number: int


@app.post("/create-tree/")
async def create_tree(data: CreateTreeData):
    root = data.nodes[0][0]
    tree = create_new_tree(root, data.nodes)
    return tree


@app.post("/find-common-ancestor/")
async def find_ancestor(data: FindAncestorData):
    root = data.nodes[0][0]
    tree = create_new_tree(root, data.nodes)
    ancestor = find_common_ancestor(tree, data.first_number, data.second_number)
    return f"ancestor({data.first_number},{data.second_number}) = {ancestor}"
