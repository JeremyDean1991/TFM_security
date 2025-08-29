import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../core_TASK/Linux_security')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../core_TASK/Joomla_security')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../core_TASK/Network_security')))

# Import all security core tasks
from clamav_core import ClamAV_CoreTask
from fail2ban_core import Fail2ban_CoreTask
from ssh_allow_deny_core import SSH_AllowDeny_CoreTask
from mod_security_core import ModSecurity_CoreTask
from mod_evasive_core import ModEvasive_CoreTask
from rootkit_hunter_core import RootKit_Hunter_CoreTask
from ports_entry_core import Ports_Entry_CoreTask
from lynis_audit_core import Lynis_audit_CoreTask
from captcha_core import Joomla_Captcha_CoreTask
from paypal_core import PayPal_CoreTask

class SecurityTaskCoordinator:
    """
    Main coordinator for all security tasks
    Provides unified interface for security operations
    """
    
    def __init__(self):
        # Initialize all security components
        self.clamav = ClamAV_CoreTask()
        self.fail2ban = Fail2ban_CoreTask()
        self.ssh_allow_deny = SSH_AllowDeny_CoreTask()
        self.mod_security = ModSecurity_CoreTask()
        self.mod_evasive = ModEvasive_CoreTask()
        self.rootkit_hunter = RootKit_Hunter_CoreTask()
        self.ports_entry = Ports_Entry_CoreTask()
        self.lynis_audit = Lynis_audit_CoreTask()
        self.captcha = Joomla_Captcha_CoreTask()
        self.paypal = PayPal_CoreTask()
    
    # ClamAV Security Methods
    def setup_clamav_security(self, LIST_file_path):
        """Setup ClamAV antivirus protection"""
        return self.clamav.setup_and_configure_clamav(LIST_file_path)
    
    def remove_clamav_security(self, LIST_file_path):
        """Remove ClamAV antivirus protection"""
        return self.clamav.remove_clamav(LIST_file_path)
    
    # Fail2ban Security Methods
    def setup_fail2ban_security(self, LIST_file_path):
        """Setup Fail2ban intrusion prevention"""
        return self.fail2ban.setup_and_configure_fail2ban(LIST_file_path)
    
    def remove_fail2ban_security(self, LIST_file_path):
        """Remove Fail2ban intrusion prevention"""
        return self.fail2ban.remove_fail2ban(LIST_file_path)
    
    # SSH Security Methods
    def setup_ssh_security(self, LIST_file_path):
        """Setup SSH access control"""
        return self.ssh_allow_deny.setup_ssh_allow_deny_hosts(LIST_file_path)
    
    def remove_ssh_security(self, LIST_file_path):
        """Remove SSH access control"""
        return self.ssh_allow_deny.remove_ssh_allow_deny_hosts(LIST_file_path)
    
    # ModSecurity Methods
    def setup_mod_security(self, LIST_file_path):
        """Setup ModSecurity WAF"""
        return self.mod_security.setup_and_configure_mod_security(LIST_file_path)
    
    def remove_mod_security(self, LIST_file_path):
        """Remove ModSecurity WAF"""
        return self.mod_security.remove_mod_security(LIST_file_path)
    
    # ModEvasive Methods
    def setup_mod_evasive(self, LIST_file_path):
        """Setup ModEvasive DDoS protection"""
        return self.mod_evasive.install_mod_evasive(LIST_file_path)
    
    def remove_mod_evasive(self, LIST_file_path):
        """Remove ModEvasive DDoS protection"""
        return self.mod_evasive.remove_mod_evasive(LIST_file_path)
    
    # RootKit Hunter Methods
    def setup_rootkit_hunter(self, LIST_file_path):
        """Setup RootKit Hunter detection"""
        return self.rootkit_hunter.install_rootkit_hunter(LIST_file_path)
    
    def run_rootkit_scan(self, LIST_file_path):
        """Run RootKit Hunter scan"""
        return self.rootkit_hunter.run_rootkit_scan(LIST_file_path)
    
    def remove_rootkit_hunter(self, LIST_file_path):
        """Remove RootKit Hunter detection"""
        return self.rootkit_hunter.remove_rootkit_hunter(LIST_file_path)
    
    # Ports Entry Methods
    def setup_ports_security(self, LIST_file_path):
        """Setup port security and firewall"""
        return self.ports_entry.configure_firewall_ports(LIST_file_path)
    
    def block_dangerous_ports(self, LIST_file_path):
        """Block dangerous ports"""
        return self.ports_entry.block_dangerous_ports(LIST_file_path)
    
    # Lynis Audit Methods
    def setup_lynis_audit(self, LIST_file_path):
        """Setup Lynis security auditing"""
        return self.lynis_audit.install_lynis(LIST_file_path)
    
    def run_lynis_audit(self, LIST_file_path):
        """Run Lynis security audit"""
        return self.lynis_audit.run_lynis_audit(LIST_file_path)
    
    def remove_lynis_audit(self, LIST_file_path):
        """Remove Lynis security auditing"""
        return self.lynis_audit.remove_lynis(LIST_file_path)
    
    # Joomla Security Methods
    def setup_joomla_captcha(self, LIST_file_path):
        """Setup Joomla Captcha protection"""
        return self.captcha.setup_and_configure_captcha(LIST_file_path)
    
    def remove_joomla_captcha(self, LIST_file_path):
        """Remove Joomla Captcha protection"""
        return self.captcha.remove_captcha(LIST_file_path)
    
    # PayPal Security Methods
    def setup_paypal_security(self, LIST_file_path):
        """Setup PayPal security configuration"""
        return self.paypal.setup_paypal_security(LIST_file_path)
    
    def remove_paypal_security(self, LIST_file_path):
        """Remove PayPal security configuration"""
        return self.paypal.remove_paypal_security(LIST_file_path)
    
    # Comprehensive Security Setup
    def setup_comprehensive_security(self, LIST_file_path):
        """
        Setup comprehensive security suite on all servers
        Includes all major security components
        """
        results = []
        log2('info', 'Starting comprehensive security setup')
        
        # Linux Security Components
        results.extend(self.setup_clamav_security(LIST_file_path))
        results.extend(self.setup_fail2ban_security(LIST_file_path))
        results.extend(self.setup_ssh_security(LIST_file_path))
        results.extend(self.setup_mod_security(LIST_file_path))
        results.extend(self.setup_mod_evasive(LIST_file_path))
        results.extend(self.setup_rootkit_hunter(LIST_file_path))
        results.extend(self.setup_ports_security(LIST_file_path))
        results.extend(self.setup_lynis_audit(LIST_file_path))
        
        # Application Security Components
        results.extend(self.setup_joomla_captcha(LIST_file_path))
        results.extend(self.setup_paypal_security(LIST_file_path))
        
        log2('info', 'Comprehensive security setup completed')
        return results
    
    def remove_comprehensive_security(self, LIST_file_path):
        """
        Remove comprehensive security suite from all servers
        """
        results = []
        log2('info', 'Starting comprehensive security removal')
        
        # Remove all security components
        results.extend(self.remove_clamav_security(LIST_file_path))
        results.extend(self.remove_fail2ban_security(LIST_file_path))
        results.extend(self.remove_ssh_security(LIST_file_path))
        results.extend(self.remove_mod_security(LIST_file_path))
        results.extend(self.remove_mod_evasive(LIST_file_path))
        results.extend(self.remove_rootkit_hunter(LIST_file_path))
        results.extend(self.remove_lynis_audit(LIST_file_path))
        results.extend(self.remove_joomla_captcha(LIST_file_path))
        results.extend(self.remove_paypal_security(LIST_file_path))
        
        log2('info', 'Comprehensive security removal completed')
        return results

