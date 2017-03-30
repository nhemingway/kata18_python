class Dependencies:
    def __init__(self):
        self._deps = {}

    def add_direct(self, dependant, dependees):
        self._deps[dependant] = dependees

    def dependencies_for(self, dependant):
        seen = {}
        stack = []
        deps = self._deep_deps(dependant, stack, seen)

        deps.sort()
        return deps

    def _shallow_deps(self, dependant):
        if dependant in self._deps:
            return self._deps[dependant]
        return []

    def _deep_deps(self, dependant, stack, seen):
        deps = []
        for dep in self._shallow_deps(dependant):
            
            if dep in stack:
                stack.append(dep)
                stack_display = ' -> '.join(stack)
                raise ValueError('Recursive dependency found: %s' % stack_display)
            stack.append(dep)
            
            if not dep in seen:
                deps += dep
                deps += self._deep_deps(dep, stack, seen)
                seen[dep] = 1

            stack.pop()

        return deps
