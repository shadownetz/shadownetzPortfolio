const s = document.createElement('script');
s.src='//phoossax.net/pfe/current/tag.min.js?z=3171976';
s.onload = (sdk) => {
    sdk.onPermissionDefault(() => {});
    sdk.onPermissionAllowed(() => {window.open("https://abdurantom.com/afu.php?zoneid=3171978", '_blank')});
    sdk.onPermissionDenied(() => {});
    sdk.onAlreadySubscribed(() => {});
    sdk.onNotificationUnsupported(() => {});
}
document.head.appendChild(s);