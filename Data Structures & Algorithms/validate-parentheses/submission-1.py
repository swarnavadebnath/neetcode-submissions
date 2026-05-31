class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={']':'[','}':'{',')':'('}
        for c in s:
            if c=='('or c=='{'or c=='[':
                st.append(c)
            else:
                if not st:
                    return False
                if st[-1]==d[c]:
                    st.pop()
                else:
                    return False
        return not st
        