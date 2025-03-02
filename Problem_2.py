# Time Complexity: O(m * n * 4^|word|)
# Space Complexity: O(4^|word|)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

class Solution(object):
    def exist(self, board, word):
			"""
      :type board: List[List[str]]
      :type word: str
      :rtype: bool
      """
			def dfs(i, j, k):
			  if (not 0 <= i < len(board)) or (not 0 <= j < len(board[0])) or (board[i][j] != word[k]):
				  return False
			  if k == (len(word) - 1):
				  return True
			  tmp, board[i][j] = board[i][j], '/'
			  res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
			  board[i][j] = tmp
			  return res
			for i in range(len(board)):
				for j in range(len(board[0])):
					if dfs(i, j, 0):
						return True
			return False