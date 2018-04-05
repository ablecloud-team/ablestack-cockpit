#!/usr/bin/env python3

import dbus
import libvirttest


class TestNetwork(libvirttest.BaseTestClass):
    """ Tests for methods and properties of the Network interface
    """
    def test_network_properties_type(self):
        """ Ensure correct return type for Network properties
        """
        _, obj = self.test_network()
        props = obj.GetAll('org.libvirt.Network', dbus_interface=dbus.PROPERTIES_IFACE)
        assert isinstance(props['Autostart'], dbus.Boolean)
        assert isinstance(props['BridgeName'], dbus.String)
        assert isinstance(props['Name'], dbus.String)
        assert isinstance(props['UUID'], dbus.String)

    def test_network_destroy(self):
        def network_stopped(path, _event):
            assert isinstance(path, dbus.ObjectPath)
            self.loop.quit()

        self.connect.connect_to_signal('NetworkEvent', network_stopped, arg1='Stopped')

        _, test_network = self.test_network()
        interface_obj = dbus.Interface(test_network, 'org.libvirt.Network')
        interface_obj.Destroy()

        self.main_loop()


if __name__ == '__main__':
    libvirttest.run()
