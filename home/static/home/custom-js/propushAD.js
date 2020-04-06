const s = document.createElement('script');
s.src='//phoossax.net/pfe/current/tag.min.js?z=3171976';
s.onload = (sdk) => {
    sdk.onPermissionDefault(() => {});
    sdk.onPermissionAllowed(() => {window.location.replace("//abdurantom.com/afu.php?zoneid=3171978")});
    sdk.onPermissionDenied(() => {window.location.replace("//abdurantom.com/afu.php?zoneid=3171978")});
    sdk.onAlreadySubscribed(() => {});
    sdk.onNotificationUnsupported(() => {});
}
document.head.appendChild(s);