# given a number of courses - n, courses are [0 - n-1]
# and course prerequisite array, find if its possible
# to finish the degree


## Cycle detection - iterate over courses, DFS to check if completable
##                 - O(V+E), O(V+E)
## Topological sorting - calculate in-degree for each course node
##                       and run a topological sort - O(V+E),O(V+E)


def canFinish(numCourses: int, prerequisites: [[int]]) -> bool:
    # Map each course to its prerequisites
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)

    # Store all courses that you want to do along the current DFS path
    visiting = set()

    def canDo(crs):
        if crs in visiting:
            # Cycle detected, already want to do the course
            return False
        if preMap[crs] == []:
            return True

        # in case the prerequisite for the course is itself
        visiting.add(crs)
        # check if this course's prerequisites can be completed
        for pre in preMap[crs]:
            if not canDo(pre):
                return False
        visiting.remove(crs)
        # course is fully possible
        preMap[crs] = []
        return True

    for c in range(numCourses):
        if not canDo(c):
            return False
    return True
