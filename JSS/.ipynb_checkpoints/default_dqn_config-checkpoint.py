config = {
    'seed': 0,
    'gamma': 0.999,
    'max_steps_per_episode': 1000,
    'replay_buffer_size': 100000,
    'epsilon': 0.9,
    'epsilon_decay':  0.995,
    'minimal_epsilon': 0.1,
    'update_network_step': 5,
    'batch_size': 64,
    'learning_rate': 5e-4,
    'tau': 1e-3,  # None to avoid clipping the value estimation
    'nb_steps': 16,
    'actors_per_cpu': 1,
    'running_sec_time': 10 * 60,
    'layer_nb': 2,
    'layer_size': 1024,
    'activation': 'tanh',
    'env_name': 'job-shop-v0',
    'instance': 'env/instances/ta51',
    'instance_path': '/JSS/JSS/env/instances/ta51',
}