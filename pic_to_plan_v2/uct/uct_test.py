from pic_to_plan_v2.uct.uct_node import Node
from pic_to_plan_v2.uct.uct import UCTSearch
import copy

uct_search = UCTSearch()

uct_search.uct_search(copy.deepcopy(uct_search.current_state_set), uct_search.possible_actions_session, iteration_limit=10)
print("done")

