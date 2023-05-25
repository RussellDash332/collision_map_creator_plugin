Code for this tutorial: http://gazebosim.org/tutorials?tut=custom_messages

## Note to self
```sh
$ gazebo ~/collision_map_creator_plugin/<world-fn>
$ ~/collision_map_creator_plugin/build/request_publisher "<UL><UR><LR><LL>" <height> <resolution> <output-fn>

$ gazebo ~/collision_map_creator_plugin/map_creator.world
$ ~/collision_map_creator_plugin/build/request_publisher "(-10,10)(10,10)(10,-10)(-10,-10)" 10 0.01 ~/map.png
```