from queue import PriorityQueue
from topspin import TopSpinState

def BWAS(start, W, B, heuristic_function, T):
    priority_queue = PriorityQueue()
    g_cost_to_reach = {start: 0}
    came_from = {}
    num_expansions = 0

    while not is_queue_empty(queue=priority_queue) and num_expansions <= T:
        current_batch = expand_batch(priority_queue=priority_queue, B=B)


def is_queue_empty(queue):
    return queue.empty()


def expand_batch(priority_queue, B):
    current_batch = []
    for _ in range(min(B, priority_queue.qsize())):
        if not is_queue_empty(queue=priority_queue):
            current_state = priority_queue.get()[1]
            current_batch.append(current_state)
    return current_batch


if __name__ == "__main__":
    start_state = TopSpinState([3, 2, 1], 2)
    state_1 = TopSpinState([2, 1, 3], 2)
    state_2 = TopSpinState([1, 3, 2], 2)
    goal_state = TopSpinState([1, 2, 3], 2)

    # Define the came_from dictionary
    came_from = {
        "goal_state": goal_state,
        "state_2": state_2,
        "state_1": state_1
    }