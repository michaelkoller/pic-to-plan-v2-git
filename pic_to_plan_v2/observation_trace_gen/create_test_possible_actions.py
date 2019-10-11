import pickle


p_a = [(1, [("act_a","","")]), \
                (1, [("act_b","bowl1","")]), \
                (1, [("act_c","bowl1","")]), \
                (1, [("act_d","bowl1","")]), \
                (1, [("act_e","bowl1","")])]

pickle.dump( p_a, open("p_a.p", "wb" ) )

