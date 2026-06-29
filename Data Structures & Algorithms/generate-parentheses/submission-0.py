class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        st = []
        def backtrack(oc,cc):
            if oc == cc == n:
                res.append("".join(st))
                return
            if oc<n:
                st.append("(")
                backtrack(oc+1,cc)
                st.pop()
            if cc<oc:
                st.append(")")
                backtrack(oc,cc+1)
                st.pop()
        backtrack(0,0)
        return res        