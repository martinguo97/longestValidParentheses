class Find_Brackect:
    def longestValidParentheses(self, s):
        inner_number=0
        left_bracket=[]
        right_bracket=[]
        inner_pair=[]
        outer_pair=[]
        left_counter=0;
        counter=0;
        right_counter=0;
        sum=0;
        inner_sum=0;
        for i in range(len(s)):
            if s[i]=='(':
                left_bracket.append(i);
                left_counter+=1
                counter+=1
            if s[i]==')' and len(left_bracket)!=0:
                right_bracket.append(i);
                right_counter+=1;
                if right_counter==left_counter-1:
                    inner_pair.append([left_bracket[counter-1],i]);"""inner pair inside an big bracket"""
                    inner_number+=1;


                if right_counter==left_counter:
                    if left_counter==1:
                        outer_pair.append([left_bracket[counter-1],i]);"""solo small outter pair found"""
                    else:
                        outer_pair.append([left_bracket[counter-right_counter],i])
                        left_counter=0;
                        right_counter=0;"""big outter bracket found"""
                else:
                    del right_bracket[-1]
                    right_counter-=1
        longest=(len(inner_pair)+len(outer_pair))*2
        print("longest is",longest)

        print(inner_pair);
        print(outer_pair);
        return longest
