class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0)   return false;
        else if(x >= 0 && x <= 9)   return true;
        else if(x >= 10){
            stringstream ss;
            ss<<x;
            string s;
            ss>>s;
            int siz = s.size();
            for(int i = 0; i <= siz; i++){
                if(i == siz-1){
                    return true;
                    break;
                }
                    
                if(s[i] == s[siz-1]){
                    siz--;
                }
                else{
                    return false;
                    break;
                }
            }
        }
        return true;
    }
};