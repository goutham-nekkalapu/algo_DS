
"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Eg: 
Input: "UD"
Output: true

"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        r_count = 0 
        l_count = 0
        u_count = 0
        d_count = 0
        for move in moves:
            if move == 'R':
                r_count += 1
            elif move == 'L':
                l_count += 1
            elif move == 'U':
                u_count += 1
            elif move == 'D':
                d_count += 1
        
        if r_count == l_count and u_count == d_count:
            return True
        else:
            return False
