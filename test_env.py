import gymnasium as gym

try:
    # 尝试导入miniworld包
    import miniworld
    print("成功导入miniworld包")
    # 尝试创建环境
    env = gym.make("MiniWorld-Maze-v0")
    print("成功创建环境: MiniWorld-Maze-v0")
    env.close()
except Exception as e:
    print(f"错误: {e}")