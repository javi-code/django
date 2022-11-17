import graphene

from .querys.querys import Query
from .mutations.mutations import Mutation 
schema = graphene.Schema(query=Query, mutation=Mutation, types=[])